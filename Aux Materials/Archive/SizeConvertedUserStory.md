### 1. User Story: Kunde - Produktgennemsyn
- **Som** kunde,
- **Ønsker jeg** at kunne se butikkens portfølje i kategorier,
- **Med det formål** bedst at kunne vælge det produkt, der opfylder mit behov.

   **Opgaver:**
   - Implementer Razor Page, der kan fremvise alle produkter i en udvalgt kategori.

   **Acceptance Criteria:**
   - *Givet* at en kunde vil se en bestemt produktkategori, *når* de leder efter et produkt der opfylder deres behov, *så* får de en tilsvarende afgrænset visning af produktkataloget.

   **Estimering:** 3

### 2. User Story: Bedemand - Speciel Ordre Funktion
- **Som** bedemand,
- **Ønsker jeg** at kunne bestille specialdesignet blomsterarrangement direkte via en dedikeret side,
- **Med det formål** at effektivisere bestillingsprocessen for begravelsesarrangementer.

   **Opgaver:**
   - Opret en dedikeret side for bedemænd med tilpassede bestillingsmuligheder.

   **Acceptance Criteria:**
   - *Givet* at en bedemand er logget ind, *når* de tilgår den dedikerede side, *så* skal de kunne vælge og tilpasse blomsterarrangementer specielt designet til begravelser.

   **Estimering:** 5

### 3. User Story: Medarbejder - Ordrehåndtering
- **Som** medarbejder,
- **Ønsker jeg** at kunne se og administrere indkommende ordrer,
- **Med det formål** at effektivisere processen for ordreklargøring og levering.

   **Opgaver:**
   - Implementer en administrationsside for medarbejdere til håndtering af ordrer.

   **Acceptance Criteria:**
   - *Givet* at en medarbejder er logget ind, *når* de tilgår administrationspanelet, *så* skal de kunne se en liste over aktive ordrer og opdatere deres status.

   **Estimering:** 3

### 4. User Story: Bestyrer - Produktadministration
- **Som** bestyrer,
- **Ønsker jeg** at kunne oprette og opdatere produkter i webshoppen,
- **Med det formål** at sikre, at produktudvalget altid er aktuelt og korrekt prissat.

   **Opgaver:**
   - Udvikle en brugergrænseflade for produktadministration i administrationspanelet.

   **Acceptance Criteria:**
   - *Givet* at en bestyrer er logget ind, *når* de tilgår produktadministrationsmodulet, *så* skal de kunne tilføje nye produkter, redigere eksisterende produkter og arkivere forældede produkter.

   **Estimering:** 5

### 5. User Story: Kunde - Ordreopfølgning
- **Som** kunde,
- **Ønsker jeg** at kunne spore status for min ordre,
- **Med det formål** at holde mig opdateret om leveringstidspunktet.

   **Opgaver:**
   - Implementer en funktion til ordreopfølgning på kundens profilside.

   **Acceptance Criteria:**
   - *Givet* at kunden har afgivet en ordre, *når* de logger ind og tjekker deres ordrestatus, *så* skal de kunne se den aktuelle status og forventet leveringstidspunkt.

   **Estimering:** 2

### 6. User Story: Bedemand - Automatisk Fakturering
- **Som** bedemand,
- **Ønsker jeg** automatisk at modtage en faktura ved bestilling,
- **Med det formål** at forenkle regnskabsprocessen.

   **Opgaver:**
   - Udvikle en automatisk faktureringsproces, der sender fakturaer direkte til bedemandens e-mail efter ordreafgivelse.

   **Acceptance Criteria:**
   - *Givet* at en bedemand afgiver en bestilling, *når* ordren er bekræftet, *så* modtager de en faktura via e-mail.

   **Estimering:** 3

### 7. User Story: Medarbejder - Lagerstyring
- **Som** medarbejder,
- **Ønsker jeg** et dashboard til at monitorere lagerstatus,
- **Med det formål** at forebygge mangler og optimere lagerbeholdningen.

   **Opgaver:**
   - Implementer et lagerstyringsmodul i medarbejderens administrationspanel.

   **Acceptance Criteria:**
   - *Givet* at en medarbejder ønsker at tjekke lagerstatus, *når* de logger ind på dashboardet, *så* skal de kunne se aktuelle lagerantal for alle produkter.

   **Estimering:** 3

### 8. User Story: Bestyrer - Salgsrapporter
- **Som** bestyrer,
- **Ønsker jeg** at kunne generere detaljerede salgsrapporter,
- **Med det formål** at analysere salgstendenser og foretage datadrevne beslutninger.

   **Opgaver:**
   - Udvikle en funktion til at generere og eksportere salgsrapporter i administrationspanelet.

   **Acceptance Criteria:**
   - *Givet* at en bestyrer ønsker at se salgsdata, *når* de vælger rapporteringsperioden og genererer rapporten, *så* præsenteres de for en detaljeret rapport over salg fordelt på produkter, kategorier og tidspunkter.

   **Estimering:** 5

### 9. User Story: Teknisk Support - Fejlhåndtering
- **Som** teknisk support,
- **Ønsker jeg** et system til effektiv fejlhåndtering,
- **Med det formål** at kunne identificere, logge og løse systemfejl hurtigt.

   **Opgaver:**
   - Implementer et værktøj for fejlrapportering og -håndtering i systemet.

   **Acceptance Criteria:**
   - *Givet* at en systemfejl opstår, *når* fejlen registreres, *så* logges den automatisk og notificerer teknisk support med detaljer om fejlen.

   **Estimering:** 3

### 10. User Story: Kunde - Gavekort og rabatkoder
- **Som** kunde,
- **Ønsker jeg** at kunne anvende gavekort og rabatkoder ved checkout,
- **Med det formål** at udnytte tilbud og spare penge på køb.

   **Opgaver:**
   - Udvikle en funktion, der tillader kunder at indløse gavekort

 og anvende rabatkoder ved betaling.

   **Acceptance Criteria:**
   - *Givet* at en kunde har et gyldigt gavekort eller rabatkode, *når* de indtaster koden ved checkout, *så* skal den pågældende rabat eller gavekortets værdi fratrækkes fra den samlede ordre.

   **Estimering:** 2

### 11. User Story: Medarbejder - Automatiske notifikationer
- **Som** medarbejder,
- **Ønsker jeg** at modtage automatiske notifikationer om nye ordrer,
- **Med det formål** at kunne påbegynde ordrebehandling så hurtigt som muligt.

   **Opgaver:**
   - Implementer en notifikationsfunktion, der alarmerer medarbejdere om nye ordrer via e-mail eller systempopup.

   **Acceptance Criteria:**
   - *Givet* at en ny ordre er afgivet, *når* ordren registreres i systemet, *så* modtager relevante medarbejdere en notifikation.

   **Estimering:** 2

### 12. User Story: Bestyrer - Brugertilpasning
- **Som** bestyrer,
- **Ønsker jeg** at kunne tilpasse og konfigurere webshop-indstillinger,
- **Med det formål** at tilpasse webshoppen til forretningsbehov og kundepræferencer.

   **Opgaver:**
   - Udvikle en konfigurationspanel for webshop-indstillinger, hvor bestyreren kan ændre indstillinger som moms, fragt, og åbningstider.

   **Acceptance Criteria:**
   - *Givet* at en bestyrer ønsker at ændre indstillinger, *når* de tilgår konfigurationspanelet, *så* skal de kunne foretage og gemme ændringer, der øjeblikkeligt træder i kraft på webshoppen.

   **Estimering:** 3

### 13. User Story: Systemadministrator - Sikkerhedsopdateringer
- **Som** systemadministrator,
- **Ønsker jeg** at kunne implementere sikkerhedsopdateringer,
- **Med det formål** at sikre systemets integritet og beskytte mod trusler.

   **Opgaver:**
   - Udvikle en proces for regelmæssig kontrol og implementering af sikkerhedsopdateringer.

   **Acceptance Criteria:**
   - *Givet* at nye sikkerhedsopdateringer er tilgængelige, *når* systemet checker for opdateringer, *så* skal opdateringerne kunne downloades og installeres automatisk eller manuelt afhængig af indstilling.

   **Estimering:** 3

### 14. User Story: Kunde - Feedback og anmeldelser
- **Som** kunde,
- **Ønsker jeg** at kunne afgive feedback og anmelde produkter,
- **Med det formål** at dele min oplevelse med andre kunder og hjælpe dem med at træffe informerede købsbeslutninger.

   **Opgaver:**
   - Implementer en feedback- og anmeldelsesfunktion på produkt siderne.

   **Acceptance Criteria:**
   - *Givet* at en kunde har købt et produkt, *når* de besøger produktets side efter købet, *så* skal de kunne skrive og indsende en anmeldelse.

   **Estimering:** 2

### 15. User Story: Site Navigering
- **Som** bruger,
- **Ønsker jeg** at kunne navigere på siden,
- **Med det formål** at se alt hvad jeg ønsker.

   **Opgaver:**
   - Udvikle et intuitivt navigationssystem på webshoppen.

   **Acceptance Criteria:**
   - *Givet* at en bruger besøger hjemmesiden, *når* de bruger navigationsmenuen, *så* kan de let finde alle ønskede sektioner.

   **Estimering:** 2

### 16. User Story: Se Produkter
- **Som** kunde,
- **Ønsker jeg** at se alle tilgængelige produkter,
- **Med det formål** at vælge et produkt.

   **Opgaver:**
   - Implementer en produktoversigtsside med alle tilgængelige produkter.

   **Acceptance Criteria:**
   - *Givet* at en kunde besøger produktoversigtssiden, *når* de kigger igennem siden, *så* skal de kunne se alle produkter, der er til salg.

   **Estimering:** 3

### 17. User Story: Produkt Detaljer
- **Som** kunde,
- **Ønsker jeg** at kunne se specifikke produktdetaljer,
- **Med det formål** at sikre, det er det rigtige produkt for mig.

   **Opgaver:**
   - Implementer en detaljeret visning for hvert produkt.

   **Acceptance Criteria:**
   - *Givet* at en kunde ser på et produkt, *når* de klikker på produktet, *så* skal de kunne se alle vigtige detaljer og beskrivelser.

   **Estimering:** 2

### 18. User Story: Oprette Konto
- **Som** kunde,
- **Ønsker jeg** at oprette og registrere en konto,
- **Med det formål** at spare tid i fremtiden ved at undgå at indtaste mine detaljer gentagne gange.

   **Opgaver:**
   - Udvikle en kontooprettelses- og registreringsproces.

   **Acceptance Criteria:**
   - *Givet* at en ny besøgende ønsker at oprette en konto, *når* de udfylder og indsender tilmeldingsformularen, *så* skal de kunne logge ind uden at skulle genindtaste deres oplysninger.

   **Estimering:** 3

### 19. User Story: Registreringsbekræftelse
- **Som** kunde,
- **Ønsker jeg** at få en bekræftelse, når jeg registrerer mig,
- **Med det formål** at vide, at jeg har gjort det korrekt (eller hvis nogen bruger min e-mail).

   **Opgaver:**
   - Sætte et bekræftelsessystem op for nyregistreringer.

   **Acceptance Criteria:**
   - *Givet* at en person forsøger at registrere sig, *når* de har indsendt deres oplysninger, *så* skal de modtage en bekræftelsesmail.

   **Estimering:** 1

### 20. User Story: Log Ind
- **Som** kunde,
- **Ønsker jeg** at logge ind,
- **Med det formål** at jeg ikke behøver at indtaste mine oplysninger igen.

   **Opgaver:**
   - Udvikle en login-funktion med e-mail og adgangskode.

   **Acceptance Criteria:**
   - *Givet* at en kunde ønsker at handle, *når* de indtaster deres loginoplysninger, *så* skal de have adgang til deres personlige konto og tidligere indtastede oplysninger.

   **Estimering:** 2

### 21. User Story: Tilføj til Kurv
- **Som** bruger,
- **Ønsker jeg** at tilføje et produkt til min kurv,
- **Med det formål** at samle min bestilling.

   **Opgaver:**
   - Implementer en funktion til at tilføje produkter til en indkøbskurv.

   **Acceptance Criteria:**
   - *Givet* at en bruger vælger et produkt, *når* de klikker på "tilføj til kurv"-knappen, *så* skal produktet blive tilføjet til deres kurv.

   **Estimering:** 2

### 22. User Story: Adgang til Kurv
- **Som** ejer,
- **Ønsker jeg** at kunden skal være logget ind for at få adgang til kurven,
- **Med det formål** at undgå anonyme køb.

   **Opgaver:**
   - Kræv at brugere logger ind før de kan tilføje produkter til kurven.

   **Acceptance Criteria:**
   - *Givet* at en kunde ønsker at tilføje produkter til en kurv, *når* de forsøger at gøre dette, *så* skal de blive bedt om at logge ind eller oprette en konto.

   **Estimering:** 3

### 23. User Story: Opret Ordre
- **Som** kunde,
- **Ønsker jeg** at skabe en ordre fra min kurv,
- **Med det formål** at købe de valgte produkter.

   **Opgaver:**
   - Udvikle en proces, hvor kunden kan omdanne indholdet af kurven til en ordre.

   **Acceptance Criteria:**
   - *Givet* at en kunde har valgt produkter i kurven, *når* de klikker på "bestil", *så* skal de kunne gennemføre købet og se en ordrebekræftelse.

   **Estimering:** 3

### 24. User Story: Opret Ny Bruger (Admin)
- **Som** administrator,
- **Ønsker jeg** at kunne oprette en ny bruger,
- **Med det formål** at administrere webstedet.

   **Opgaver:**
   - Udvikle en admin-funktion til at oprette nye brugerkonti.

   **Acceptance Criteria:**
   - *Givet* at en administrator har brug for at oprette en ny bruger, *når* de indtaster nødvendige brugeroplysninger i adminpanelet, *så* skal et nyt brugerlogin kunne oprettes.

   **Estimering:** 3

### 25. User Story: Ordreoversigt (Medarbejder)
- **Som** medarbejder,
- **Ønsker jeg** at kunne se alle ordrer,
- **Med det formål** at få et overblik over arbejdsbyrden.

   **Opgaver:**
   - Udvikle et dashboard, hvor medarbejdere kan se en liste over alle aktuelle ordrer.

   **Acceptance Criteria:**
   - *Givet* at en medarbejder er logget ind, *når* de tilgår dashboardet, *så* skal de kunne se og sortere alle ordrer efter status, dato og andre relevante kriterier.

   **Estimering:** 3

### 26. User Story: Gennemse Nye Ordrer (Medarbejder)
- **Som** medarbejder,
- **Ønsker jeg** at gennemgå nye ordrer,
- **Med det formål** at kunne acceptere eller afvise dem.

   **Opgaver:**
   - Implementer en funktion, hvor medarbejdere kan gennemse og administrere nye ordrer.

   **Acceptance Criteria:**
   - *Givet* at en ny ordre er modtaget, *når* medarbejderen gennemgår ordren, *så* skal de kunne træffe en beslutning om at acceptere eller afvise ordren baseret på lagerbeholdning og andre faktorer.

   **Estimering:** 2

### 27. User Story: Ordreansvar (Medarbejder)
- **Som** medarbejder,
- **Ønsker jeg** at kunne tildele en ordre til mig selv,
- **Med det formål** at sikre ansvarsfordelingen for ordrehåndteringen.

   **Opgaver:**
   - Udvikle et system, hvor medarbejdere kan tildele specifikke ordrer til sig selv for håndtering.

   **Acceptance Criteria:**
   - *Givet* at en ordre skal behandles, *når* en medarbejder vælger ordren, *så* skal de kunne markere den som "under behandling" af sig selv.

   **Estimering:** 2

### 28. User Story: Ordreklargøring (Medarbejder)
- **Som** medarbejder,
- **Ønsker jeg** at markere en ordre som klar til afhentning og fuldført,
- **Med det formål** at administrere ordreflowet effektivt.

   **Opgaver:**
   - Skab en funktion, hvor medarbejdere kan opdatere ordrens status til "klar til afhentning" og senere "afhentet".

   **Acceptance Criteria:**
   - *Givet* at en ordre er færdigpakket, *når* medarbejderen opdaterer systemet, *så* skal statussen ændres, så kunden og andre medarbejdere kan se, at ordren er klar eller afhentet.

   **Estimering:** 2

### 29. User Story: Ændre Ordre i Kurv (Bruger)
- **Som** bruger,
- **Ønsker jeg** at ændre mængden af produkter i min kurv,
- **Med det formål** at justere min bestilling før køb.

   **Opgaver:**
   - Implementer en redigeringsfunktion i kurven, hvor brugeren kan opdatere antallet eller fjerne produkter fra kurven.

   **Acceptance Criteria:**
   - *Givet* at en bruger ønsker at ændre sin bestilling, *når* de besøger kurvsiden, *så* skal de kunne ændre antallet af produkter eller fjerne dem fra kurven.

   **Estimering:** 1

### 30. User Story: Opdater Bruger (Admin)
- **Som** administrator,
- **Ønsker jeg** at kunne opdatere eksisterende brugere,
- **Med det formål** at administrere webstedet effektivt.

   **Opgaver:**
   - Skabe en funktion i adminpanelet, der tillader redigering af brugerkonti.

   **Acceptance Criteria:**
   - *Givet* at en bruger skal have opdateret deres information, *når* administratoren indtaster de nye oplysninger i systemet, *så* skal disse ændringer afspejles på brugerens konto.

   **Estimering:** 2

### 31. User Story: Slet Bruger (Admin)
- **Som** administrator,
- **Ønsker jeg** at kunne slette en bruger,
- **Med det formål** at kunne administrere medarbejdere, bedemænd og kunder.

   **Opgaver:**
   - Implementer en slet-funktion i adminpanelet for brugere.

   **Acceptance Criteria:**
   - *Givet* at en bruger ikke længere skal have adgang til systemet, *når* administratoren sletter brugeren, *så* skal brugerens konto ikke længere være aktiv eller tilgængelig.

   **Estimering:** 1

### 32. User Story: Produktopdatering (Medarbejder)
- **Som** medarbejder,
- **Ønsker jeg** at opdatere produkter,
- **Med det formål** at styre lagerbeholdningen.

   **Opgaver:**
   - Udvikle et interface til opdatering af produktinformationer og lagerstatus.

   **Acceptance Criteria:**
   - *Givet* at et produkt behøver en opdatering, *når* medarbejderen ændrer informationen i systemet, *så* skal disse ændringer være synlige på webshoppen.

   **Estimering:** 3

### 33. User Story: Opret Nyt Produkt (Medarbejder/Administrator)
- **Som** medarbejder/administrator,
- **Ønsker jeg** at kunne oprette et nyt produkt,
- **Med det formål** at holde produktkataloget opdateret med nye varer.

   **Opgaver:**
   - Skabe en tilføj produkt-funktion på webshoppen for medarbejdere og administratorer.

   **Acceptance Criteria:**
   - *Givet* at webshoppen skal have nye produkter tilføjet, *når* medarbejder/administrator indtaster produktdetaljerne og uploader billeder, *så* skal det nye produkt være tilgængeligt i webshoppen.

   **Estimering:** 3

### 34. User Story: Deaktiver Produkt (Medarbejder/Administrator)
- **Som** medarbejder/administrator,
- **Ønsker jeg** at kunne deaktivere et produkt,
- **Med det formål** at fjerne gamle produkter fra produktkataloget.

   **Opgaver:**
   - Implementer en funktion til at deaktivere produkter i produktoversigten.

   **Acceptance Criteria:**
   - *Givet* at et produkt ikke længere skal sælges, *når* medarbejder/administrator deaktiverer produktet i systemet, *så* skal produktet ikke længere være synligt for kunder.

   **Estimering:** 2

### 35. User Story: Ordrefilter og -sortering (Medarbejder)
- **Som** medarbejder,
- **Ønsker jeg** at filtrere og sortere ordrer,
- **Med det formål** at få et overblik over ordrer, der er forfaldne eller som jeg er ansvarlig for.

   **Opgaver:**
   - Oprette filter- og sorteringsfunktioner i ordreoversigten.

   **Acceptance Criteria:**
   - *Givet* at der er behov for at organisere ordrer, *når* medarbejderen anvender filter- og sorteringsfunktionerne, *så* skal de kunne se en organiseret liste over ordrer.

   **Estimering:** 2

### 36. User Story: Produktfiltrering (Kunde)
- **Som** kunde,
- **Ønsker jeg** at kunne filtrere produkter på produktsiden,
- **Med det formål** nemt at finde det rigtige produkt.

   **Opgaver:**
   - Tilføje filtreringsmuligheder på produktsiden.

   **Acceptance Criteria:**
   - *Givet* at en kunde søger efter et specifikt produkt, *når* de bruger filterfunktionerne, *så* skal de kunne se en filtreret liste af produkter, der matcher deres kriterier.

   **Estimering:** 3

### 37. User Story: Ordrenotifikationer (Medarbejder)
- **Som** medarbejder,
- **Ønsker jeg** at modtage en notifikation fra systemet, når en ny ordre indsendes,
- **Med det formål** at kunne ekspedere ordren hurtigt.

   **Opgaver:**
   - Implementere et system til at sende automatisk notifikation til medarbejderne om nye ordrer.

   **Acceptance Criteria:**
   - *Givet* at en ny ordre er indsendt, *når* systemet registrerer ordren, *så* skal medarbejderne modtage en notifikation.

   **Estimering:** 2

### 38. User Story: Leveringsvalg (Bedemand)
- **Som** bedemand,
- **Ønsker jeg** at kunne vælge leveringssted og -tid,
- **Med det formål** at kunne drive min forretning.

   **Opgaver:**
   - Skabe et brugerinterface, hvor bedemænd kan vælge leveringsdetaljer ved bestilling.

   **Acceptance Criteria:**
   - *Givet* at en bedemand laver en bestilling, *når* de indtaster leveringsoplysninger, *så* skal disse oplysninger anvendes til ordren.

   **Estimering:** 3

### 39. User Story: Genskabe Produkt (Medarbejder)
- **Som** medarbejder,
- **Ønsker jeg** at kunne se deaktiverede produkter og genaktivere dem,
- **Med det formål** at administrere produktkataloget.

   **Opgaver:**
   - Tilføje en funktion til at se og reaktivere deaktiverede produkter.

   **Acceptance Criteria:**
   - *Givet* at et produkt tidligere er blevet deaktiveret, *når* medarbejderen ønsker at genaktivere det, *så* skal produktet igen kunne vises og sælges på hjemmesiden.

   **Estimering:** 2

### 40. User Story: Kurvindikator (Kunde)
- **Som** kunde,
- **Ønsker jeg** at se antallet af produkter i min kurv uden at være på kurvsiden,
- **Med det formål** at kunne holde styr på mine valgte varer med lethed.

   **Opgaver:**
   - Tilføj en indikator på hjemmesiden, der viser antal produkter i kurven.

   **Acceptance Criteria:**
   - *Givet* at en kunde har tilføjet produkter til deres kurv, *når* de navigerer væk fra kurvsiden, *så* skal de stadig kunne se en indikator med antal produkter i kurven.

   **Estimering:** 1

### 41. User Story: Redigering af Statisk Indhold (Medarbejder/Administrator)
- **Som** medarbejder/administrator,
- **Ønsker jeg** at kunne redigere statiske elementer på hjemmesiden,
- **Med det formål** at opdatere informationer.

   **Opgaver:**
   - Implementer en redigeringsfunktion for statisk indhold på hjemmesiden.

   **Acceptance Criteria:**
   - *Givet* at statisk indhold på hjemmesiden kræver opdatering, *når* medarbejder/administrator redigerer indholdet gennem et administrativt interface, *så* skal ændringerne blive vist på hjemmesiden.

   **Estimering:** 3

### 42. User Story: Navigation i Profil (Kunde)
- **Som** kunde,
- **Ønsker jeg** at kunne navigere nemt på mine profilsider,
- **Med det formål** at brugeroplevelsen føles glidende og uforstyrret.

   **Opgaver:**
   - Design en brugervenlig og intuitiv grænseflade for kundens profilområde.

   **Acceptance Criteria:**
   - *Givet* at en kunde ønsker at administrere sin profil, *når* de navigerer på deres profil, *så* skal de kunne gøre det uden forvirring eller forstyrrelser.

   **Estimering:** 2

### 43. User Story: Tekstsøgning efter Produkter (Kunde)
- **Som** kunde,
- **Ønsker jeg** at søge efter produkter med tekst,
- **Med det formål** at hurtigt finde, hvad jeg har i tankerne.

   **Opgaver:**
   - Integrer en søgefunktion i webshoppen, som tillader tekstbaseret søgning.

   **Acceptance Criteria:**
   - *Givet* at en kunde ved, hvad de leder efter, *når* de indtaster søgekriterier, *så* skal de præsenteres for relevante produktresultater.

   **Estimering:** 3

### 44. User Story: Visning af Søgeresultater (Bruger)
- **Som** bruger,
- **Ønsker jeg** at kunne se mine søgeresultater,
- **Med det formål** at kunne vælge et produkt fra resultaterne.

   **Opgaver:**
   - Skabe en visning, der effektivt præsenterer resultaterne af en produktsøgning.

   **Acceptance Criteria:**
   - *Givet* at en bruger har foretaget en søgning, *når* søgeresultaterne vises, *så* skal de være klare og lette at navigere i.

   **Estimering:** 2

### 45. User Story: Sortering og Filtrering af Søgeresultater (Bruger)
- **Som** bruger,
- **Ønsker jeg** at kunne sortere og filtrere søgeresultaterne efter en produktsøgning,
- **Med det formål** bedre at finde det, jeg leder efter.

   **Opgaver:**
   - Tilføj sortering og filtreringsmuligheder til søgeresultatsiden.

   **Acceptance Criteria:**
   - *Givet* at en bruger har udført en søgning og ser på resultaterne, *når* de anvender filtrerings- og sorteringsfunktionerne, *så* skal listen over produkter opdatere sig i henhold til de valgte kriterier.

   **Estimering:** 3

### 46. User Story: Log Ind på Ordreportal (Medarbejder)
- **Som** medarbejder,
- **Ønsker jeg** at kunne logge ind på ordreportalen,
- **Med det formål** at kunne ekspedere ordrer.

   **Opgaver:**
   - Implementer en sikker log ind-funktion specifikt for medarbejdere på ordreportalen.

   **Acceptance Criteria:**
   - *Givet* at en medarbejder står foran sin arbejdsstation, *når* de indtaster deres legitimationsoplysninger, *så* skal de have adgang til ordreportalen, hvor de kan administrere ordrer.

   **Estimering:** 2

### 47. User Story: Se Ordredetaljer (Medarbejder)
- **Som** medarbejder,
- **Ønsker jeg** at kunne se ordredetaljer om blomsterarrangementet,
- **Med det formål** at kunne ekspedere ordrer korrekt og effektivt.

   **Opgaver:**
   - Udvikle en funktion, der viser fulde detaljer for hver ordre, inklusive specifikationer for blomsterarrangementet.

   **Acceptance Criteria:**
   - *Givet* at en medarbejder behandler en ordre, *når* de tilgår ordren på systemet, *så* skal de kunne se alle relevante detaljer om blomsterarrangementet, som er nødvendige for at færdiggøre ordren korrekt.

   **Estimering:** 3

### 48. User Story: Opdatere Ordrestatus (Medarbejder)
- **Som** medarbejder,
- **Ønsker jeg** at kunne opdatere ordrestatus,
- **Med det formål** at tydeliggøre for alle brugere, hvor langt ordren er i processen.

   **Opgaver:**
   - Skabe en funktion, der tillader medarbejdere at opdatere status for en ordre i realtid.

   **Acceptance Criteria:**
   - *Givet* at en ordre er i gang med at blive ekspederet, *når* medarbejderen opdaterer ordrens status, *så* skal denne opdatering være synlig for alle relevante parter, herunder andre medarbejdere og kunden, hvis de tjekker status online.

   **Estimering:** 3