# Nordvik Fastigheter – Azure Examination

Det här projektet är en felanmälningsportal för Nordvik Fastigheter som jag har byggt under min Azure-examination.

## Teknik och tjänster
- **Azure Virtual Machine:** Ubuntu-server där webbportalen körs.
- **Nginx:** Används som webbserver.
- **Python och Flask:** Backend som tar emot felanmälningar.
- **Azure Blob Storage:** Lagrar uppladdade bilder.
- **Managed Identity och RBAC:** Ger servern åtkomst till lagringen utan att behöva spara lösenord i koden.
- **Power Automate:** Hanterar inkommande HTTP-begäranden.
- **Microsoft Lists/SharePoint:** Sparar felanmälningar.
- **Microsoft Teams:** Skickar meddelanden om nya felanmälningar.

## Så fungerar lösningen
Tanken är att en användare ska kunna skicka en felanmälan via webbportalen. Flask tar emot informationen och hanterar bilduppladdningen till Blob Storage.

Jag har även skapat ett Power Automate-flöde som kan ta emot en HTTP-begäran, skapa ett objekt i SharePoint-listan och skicka en avisering till Teams. Flödet har testats separat med PowerShell.

## Filer
- `index.html` – webbportalens HTML-kod.
- `ARM-template.json` – ARM-mall för Azure-resurser.

## Testning
Jag har testat Flask och uppladdning till Blob Storage via terminalen. Jag har även testat Power Automate med en HTTP-begäran från PowerShell och kontrollerat att flödet kördes utan fel.
