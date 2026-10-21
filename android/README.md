# PokéVault Android
App Android con WebView persistente che visualizza https://andremgsnake.github.io/pokevault/ e permette di importare file CSV tramite il selettore documenti Android.

## Generare l'APK
GitHub -> Actions -> Build PokéVault Android APK -> Run workflow. Dopo un build riuscito scaricare l'artifact PokeVault-Android-APK, estrarre lo ZIP e installare app-debug.apk sul proprio telefono.

L'APK è **debug-signed**: per distribuire una release ufficiale serve una firma release privata e un processo di aggiornamento. La collezione è memorizzata nello storage WebView specifico dell'app e non si trasferisce automaticamente da Chrome. Importare nuovamente il CSV nell'app. La connessione internet è necessaria per i prezzi.
