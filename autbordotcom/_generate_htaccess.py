#! python3
# Generates the autbor.com URL shortcuts for the .htaccess file

TEMPLATE = 'RewriteRule ^%s$ %s [L]'

URLS = {# CHAPTER 0-6:
        # CHAPTER 7 - Regex:
        'teachregex':           'http://www.theguardian.com/technology/2012/dec/04/ict-teach-kids-regular-expressions',
        'regex':                '',
        'bitwise':              '',
        'htmlregex':            'http://stackoverflow.com/a/1732454/1893164',
        # CHAPTER 8 - File I/O:
        # CHAPTER 9 - File Handling:
        # CHAPTER 10 - Debugging:
        # CHAPTER 11 - Web Scraping:
        'pragmaticunicode':     'http://nedbatchelder.com/text/unipain.html',
        'joelunicode':          'http://www.joelonsoftware.com/articles/Unicode.html',
        'example.html':         'http://automatetheboringstuff.com/src/example.html',
        # CHAPTER 12 - Excel
        'example.xlsx':         'http://automatetheboringstuff.com/src/example.xlsx',
        # CHAPTER 13 - PDF/Word
        'pdfmetadata':          'http://www.verypdf.com/pdfinfoeditor/pdf-information-manager.html',
        # CHAPTER 14 - CSV/JSON
        'JSONAPIs':             'http://www.programmableweb.com/category/all/apis?data_format=21173',
        'excelSpreadsheets.zip':'', # I DON'T HAVE THIS FILE.
        # CHAPTER 15 - Time/Threads
        'threadworms':          'http://inventwithpython.com/blog/2013/04/22/multithreaded-python-tutorial-with-threadworms/',
        'schedulers':           '',
        'strftime':             'http://strftime.net/',
        # CHAPTER 16 - Email/Text
        'gmail':                'https://support.google.com/accounts/answer/185833', # app-specific passwords
        'gmail_search':         '',
        'sms':                  'https://www.twilio.com/blog/2014/05/send-and-receive-sms-messages-via-email-with-twilio-and-sendgrid.html',
        'twiliostatus':         'https://www.twilio.com/docs/api/rest/message#error-values',
        # CHAPTER 17 - Images
        'colors':               '',
        # CHAPTER 18 - GUI Automation
        'sushi':                'http://code.tutsplus.com/tutorials/how-to-build-a-python-bot-that-can-play-web-games--active-11117',
        'form':                 'https://docs.google.com/forms/d/1A39NpQYMN8OOG-_lqDLFQb2h1SiHhCxPh0udtDEy2rU/viewform?usp=send_form',

        # FILES
        'alarm.wav':            'http://automatetheboringstuff.com/src/alarm.wav',
        'allMyCats1.py':        'http://automatetheboringstuff.com/src/allMyCats1.py',
        'allMyCats2.py':        'http://automatetheboringstuff.com/src/allMyCats2.py',
        'backupToZip.py':       'http://automatetheboringstuff.com/src/backupToZip.py',
        'birthdays.py':         'http://automatetheboringstuff.com/src/birthdays.py',
        'boxprint.py':          'http://automatetheboringstuff.com/src/boxprint.py',
        'bulletpointadder.py':  'http://automatetheboringstuff.com/src/bulletpointadder.py',
        'calcprod.py':          'http://automatetheboringstuff.com/src/calcprod.py',
        'catnapping.py':        'http://automatetheboringstuff.com/src/catnapping.py',
        'census2010.py':        'http://automatetheboringstuff.com/src/census2010.py',
        'censuspopdata.xlsx':   'http://automatetheboringstuff.com/src/censuspopdata.xlsx',
        'characterCount.py':    'http://automatetheboringstuff.com/src/characterCount.py',
        'coinFlip.py':          'http://automatetheboringstuff.com/src/coinFlip.py',
        'combinePDFs.py':       'http://automatetheboringstuff.com/src/combinePDFs.py',
        'combinedminutes.pdf':  'http://automatetheboringstuff.com/src/combinedminutes.pdf',
        'countdown.py':         'http://automatetheboringstuff.com/src/countdown.py',
        'debugExample.py':      'http://automatetheboringstuff.com/src/debugExample.py',
        'demo.docx':            'http://automatetheboringstuff.com/src/demo.docx',
        'dictionary.txt':       'http://automatetheboringstuff.com/src/dictionary.txt',
        'dimensions.xlsx':      'http://automatetheboringstuff.com/src/dimensions.xlsx',
        'downloadxkcd.py':      'http://automatetheboringstuff.com/src/downloadxkcd.py',
        'duesRecords.xlsx':     'http://automatetheboringstuff.com/src/duesRecords.xlsx',
        'encrypted.pdf':        'http://automatetheboringstuff.com/src/encrypted.pdf',
        'encryptedminutes.pdf': 'http://automatetheboringstuff.com/src/encryptedminutes.pdf',
        'errorExample.py':      'http://automatetheboringstuff.com/src/errorExample.py',
        'example.csv':          'http://automatetheboringstuff.com/src/example.csv',
        'example.zip':          'http://automatetheboringstuff.com/src/example.zip',
        'factorialLog.py':      'http://automatetheboringstuff.com/src/factorialLog.py',
        'formFiller.py':        'http://automatetheboringstuff.com/src/formFiller.py',
        'freezeExample.xlsx':   'http://automatetheboringstuff.com/src/freezeExample.xlsx',
        'getDocxText.py':       'http://automatetheboringstuff.com/src/getDocxText.py',
        'guessTheNumber.py':    'http://automatetheboringstuff.com/src/guessTheNumber.py',
        'guests.txt':           'http://automatetheboringstuff.com/src/guests.txt',
        'headings.docx':        'http://automatetheboringstuff.com/src/headings.docx',
        'hello.py':             'http://automatetheboringstuff.com/src/hello.py',
        'helloFunc.py':         'http://automatetheboringstuff.com/src/helloFunc.py',
        'helloFunc2.py':        'http://automatetheboringstuff.com/src/helloFunc2.py',
        'helloworld.docx':      'http://automatetheboringstuff.com/src/helloworld.docx',
        'inventory.py':         'http://automatetheboringstuff.com/src/inventory.py',
        'isPhoneNumber.py':     'http://automatetheboringstuff.com/src/isPhoneNumber.py',
        'lucky.py':             'http://automatetheboringstuff.com/src/lucky.py',
        'magic8ball.py':        'http://automatetheboringstuff.com/src/magic8ball.py',
        'magic8ball2.py':       'http://automatetheboringstuff.com/src/magic8ball2.py',
        'mapit.py':             'http://automatetheboringstuff.com/src/mapit.py',
        'mcb.pyw':              'http://automatetheboringstuff.com/src/mcb.pyw',
        'meetingminutes.pdf':   'http://automatetheboringstuff.com/src/meetingminutes.pdf',
        'meetingminutes2.pdf':  'http://automatetheboringstuff.com/src/meetingminutes2.pdf',
        'merged.xlsx':          'http://automatetheboringstuff.com/src/merged.xlsx',
        'morning-glory.jpg':    'http://automatetheboringstuff.com/src/morning-glory.jpg',
        'mouseNow.py':          'http://automatetheboringstuff.com/src/mouseNow.py',
        'mouseNow2.py':         'http://automatetheboringstuff.com/src/mouseNow2.py',
        'multidownloadxkcd.py': 'http://automatetheboringstuff.com/src/multidownloadxkcd.py',
        'multipleParagraphs.docx': 'http://automatetheboringstuff.com/src/multipleParagraphs.docx',
        'myPets.py':            'http://automatetheboringstuff.com/src/myPets.py',
        'passingReference.py':  'http://automatetheboringstuff.com/src/passingReference.py',
        'phoneandemail.py':     'http://automatetheboringstuff.com/src/phoneandemail.py',
        'picnicTable.py':       'http://automatetheboringstuff.com/src/picnicTable.py',
        'prettyCharacterCount.py': 'http://automatetheboringstuff.com/src/prettyCharacterCount.py',
        'produceSales.xlsx':    'http://automatetheboringstuff.com/src/produceSales.xlsx',
        'pw.py':                'http://automatetheboringstuff.com/src/pw.py',
        'quickweather.py':      'http://automatetheboringstuff.com/src/quickweather.py',
        'randomQuizGenerator.py': 'http://automatetheboringstuff.com/src/randomQuizGenerator.py',
        'readCensusExcel.py':   'http://automatetheboringstuff.com/src/readCensusExcel.py',
        'removeBorder.py':      'http://automatetheboringstuff.com/src/removeBorder.py',
        'removeCsvHeader.py':   'http://automatetheboringstuff.com/src/removeCsvHeader.py',
        'removeCsvHeader.zip':  'http://automatetheboringstuff.com/src/removeCsvHeader.zip',
        'renameDates.py':       'http://automatetheboringstuff.com/src/renameDates.py',
        'resizeAndAddLogo.py':  'http://automatetheboringstuff.com/src/resizeAndAddLogo.py',
        'restyled.docx':        'http://automatetheboringstuff.com/src/restyled.docx',
        'sameName.py':          'http://automatetheboringstuff.com/src/sameName.py',
        'sameName2.py':         'http://automatetheboringstuff.com/src/sameName2.py',
        'sameName3.py':         'http://automatetheboringstuff.com/src/sameName3.py',
        'sameName4.py':         'http://automatetheboringstuff.com/src/sameName4.py',
        'sampleChart.xlsx':     'http://automatetheboringstuff.com/src/sampleChart.xlsx',
        'sendDuesReminders.py': 'http://automatetheboringstuff.com/src/sendDuesReminders.py',
        'stopwatch.py':         'http://automatetheboringstuff.com/src/stopwatch.py',
        'styled.xlsx':          'http://automatetheboringstuff.com/src/styled.xlsx',
        'styles.xlsx':          'http://automatetheboringstuff.com/src/styles.xlsx',
        'textmyself.py':        'http://automatetheboringstuff.com/src/textmyself.py',
        'threadDemo.py':        'http://automatetheboringstuff.com/src/threadDemo.py',
        'tictactoe-example1.py': 'http://automatetheboringstuff.com/src/tictactoe-example1.py',
        'torrentStarter.py':    'http://automatetheboringstuff.com/src/torrentStarter.py',
        'twoPage.docx':         'http://automatetheboringstuff.com/src/twoPage.docx',
        'updateProduce.py':     'http://automatetheboringstuff.com/src/updateProduce.py',
        'updatedProduceSales.xlsx': 'http://automatetheboringstuff.com/src/updatedProduceSales.xlsx',
        'vampire.py':           'http://automatetheboringstuff.com/src/vampire.py',
        'watermark.pdf':        'http://automatetheboringstuff.com/src/watermark.pdf',
        'zeroDivide.py':        'http://automatetheboringstuff.com/src/zeroDivide.py',
        'zophie.png':           'http://automatetheboringstuff.com/src/zophie.png',

}

print('RewriteEngine on')
for k, v in URLS.items():
    print(TEMPLATE % (k, v))