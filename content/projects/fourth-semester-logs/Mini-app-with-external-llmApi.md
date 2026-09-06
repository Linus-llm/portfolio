+++
date = '2026-09-06T17:06:24+01:00'
draft = false
title = 'external llm-api application'
+++

Design af rubrikken. Jeg har kigget de tre udleverede filer igennem og jeg har bestemt at rubrikken skal vurdere opgaven mere på krav-til-rapport.md, laeringsmaal.md og mindre på dare-share-care.md. 
Det vil altså sige at jeg har beskrevet det til Codex at jeg vægter de to andre filer højere i vurderingssammenhængen og den foreslog at vægte dare-share-care med 20% ud af 100%. Sådan her er den opbygget:
Rapportens obligatoriske indhold: 25 point
Viden: 10 point
Færdigheder: 25 point
Kompetencer: 20 point
DARE, SHARE, CARE: 20 point

Hvert underkriterium ud fra de fire punkter har en vægt den vægt ganges med:
Utilstrækkelig = 0,25
Grundlæggende = 0,50
Kompetent = 0,75
Fremragende = 1,00

Deres point bliver lagt sammen tilsidst og ud fra deres samlede point gives der en karakter

90–100 = 12
80–89 = 10
65–79 = 7
50–64 = 4
40–49 = 02
20–39 = 00
0–19 = -3

Hvis der mangler obligatorisk indhold bliver karakteren sat til 00. 

-------------------------------------------------------------------------

design af systemprompt:

Du er en evaluerings expert som skal vurdere students opgave ud fra rubrikken du har modtaget. I rubrikken vil der være tydeligt defineret regler som du skal evaluere og vurdere student på. Du skal holde evaluering til kun rubrikken og ikke udenfra kommende viden. Dit svar skal give en samlet vurdering som der også er i rubrikken. Du skal komme med styrker, svagheder og foreslag til forbedringer. Svaret skal returneres som JSON. Det du modtager er også JSON.

Det er hvad jeg selv har kommet med og beder nu chatgpt til at komme med ændringer til forslag i den.

Du er en evalueringsassistent, der skal foretage en vejledende vurdering af en studerendes opgave.

Du modtager:
1. en rubric i JSON-format
2. en studenteropgave

Du skal vurdere opgaven udelukkende ud fra kriterierne og reglerne i den modtagne rubric.

Regler:
- Brug kun information, der findes i studenteropgaven og rubrikken.
- Du må ikke opfinde evidens eller antage information, som ikke fremgår af opgaven.
- Hvis der ikke er tilstrækkelig evidens til at vurdere et kriterium, skal dette fremgå tydeligt.
- Vurder hvert kriterium separat.
- Brug kun de vurderingsniveauer, der er defineret i rubrikken.
- Følg criterionId og level-id'er præcist som de står i rubrikken.
- Giv kort og konkret evidens fra opgaven for hver vurdering.
- Giv styrker og forslag til forbedringer.
- Giv en samlet tekstlig vurdering.
- Vurderingen er vejledende og erstatter ikke en faglig bedømmelse fra eksaminator eller censor.

Du må ikke selv ændre rubrikkens kriterier, vægte eller vurderingsniveauer.

Returner KUN gyldig JSON.
Returner ingen Markdown, ingen forklarende tekst før eller efter JSON og ingen ```json-kodeblok.

Svaret skal følge dette format:

{
  "criteria": [
    {
      "criterionId": "string",
      "level": "string",
      "evidence": ["string"],
      "strengths": ["string"],
      "improvements": ["string"]
    }
  ],
  "overallSummary": "string",
  "overallStrengths": ["string"],
  "overallWeaknesses": ["string"],
  "followUpQuestions": ["string"]
}

--------------------------------------------------------------

Desing af backend:

Service.java står for at sende mit userPrompt og systemPrompt til api'et og hente et svar tilbage fra den eksterne llm. (sker med httpsrequests)
Den metode som er I Service bliver kaldt i min Main klasse pt, og vi opbevarer svaret i et string. 
Derefter opretter jeg et DTO objekt som er llm's evaluering. Den evaluering sendes sammen med rubikken ind i EvaluationCalculator som holder kriterierne fra rubikken op mod llm's evaluering, hvilket giver mig et nyt DTO objekt FinalEvaluationDTO der består af:
- totalScore 
- rubric max points
- suggestedGrade
- results
- overall summary
- overall strengths
- overall weakness
- follow up questions. 

Så det vigtige ved det her design er helt klart min systemprompt, hvilket er afgørende for at kunne holde llm's evaluering op mod rubrikkens kriterier. Hvis systemprompten ikke er meget specifik, kan llm'en finde på at ændrer responset for hver gang. 

For at have en ekstra sikkerhed mod JSON fejl fra llm responset, har jeg fået codex til at lave en klasse (LlmResponseValidator) og metode der tjekker ting som:
- er svaret tomt
- et kriterie mangler
- kriteriet optræder flere gange

applikation kan nu bruge en af de studenter opgaver der er lagt i resources, sende et request til openAI api behandle responset og tjekke om det er gyldigt til en hvis grad. Komme med en endelig evaluering og printe det I terminalen.
Programmet er blevet kørt igennem adskillige gange og giver samme output.
