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
        # CHAPTER 12 - Excel
        'readCensusExcel.py':   '',
        'readExcelCensus.py':   '',
        # CHAPTER 13 - PDF/Word
        'pdfmetadata':          'http://www.verypdf.com/pdfinfoeditor/pdf-information-manager.html',
        # CHAPTER 14 - CSV/JSON
        'removeCsvHeader.zip':  '',
        'JSONAPIs':             '',
        'excelSpreadsheets.zip':'',
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
        'sushi':                '',
        'form':                 'https://docs.google.com/forms/d/1A39NpQYMN8OOG-_lqDLFQb2h1SiHhCxPh0udtDEy2rU/viewform?usp=send_form',

        # FILES
        'alarm.wav':            'http://automatetheboringstuffwithpython.com/src/alarm.wav',
        'allMyCats1.py':        'http://automatetheboringstuffwithpython.com/src/allMyCats1.py',
        'allMyCats2.py':        'http://automatetheboringstuffwithpython.com/src/allMyCats2.py',
        'backupToZip.py':       'http://automatetheboringstuffwithpython.com/src/backupToZip.py',
        'birthdays.py':         'http://automatetheboringstuffwithpython.com/src/birthdays.py',
        'boxprint.py':          'http://automatetheboringstuffwithpython.com/src/boxprint.py',
        'bulletpointadder.py':  'http://automatetheboringstuffwithpython.com/src/bulletpointadder.py',
        'calcprod.py':          'http://automatetheboringstuffwithpython.com/src/calcprod.py',
        'catnapping.py':        'http://automatetheboringstuffwithpython.com/src/catnapping.py',
        'census2010.py':        'http://automatetheboringstuffwithpython.com/src/census2010.py',
        'censuspopdata.xlsx':   'http://automatetheboringstuffwithpython.com/src/censuspopdata.xlsx',
        'characterCount.py':    'http://automatetheboringstuffwithpython.com/src/characterCount.py',
        'coinFlip.py':          'http://automatetheboringstuffwithpython.com/src/coinFlip.py',
        'combinePDFs.py':       'http://automatetheboringstuffwithpython.com/src/combinePDFs.py',
        'combinedminutes.pdf':  'http://automatetheboringstuffwithpython.com/src/combinedminutes.pdf',
        'countdown.py':         'http://automatetheboringstuffwithpython.com/src/countdown.py',
        'debugExample.py':      'http://automatetheboringstuffwithpython.com/src/debugExample.py',
        'demo.docx':            'http://automatetheboringstuffwithpython.com/src/demo.docx',
        'dictionary.txt':       'http://automatetheboringstuffwithpython.com/src/dictionary.txt',
        'dimensions.xlsx':      'http://automatetheboringstuffwithpython.com/src/dimensions.xlsx',
        'downloadxkcd.py':      'http://automatetheboringstuffwithpython.com/src/downloadxkcd.py',
        'duesRecords.xlsx':     'http://automatetheboringstuffwithpython.com/src/duesRecords.xlsx',
        'encrypted.pdf':        'http://automatetheboringstuffwithpython.com/src/encrypted.pdf',
        'encryptedminutes.pdf': 'http://automatetheboringstuffwithpython.com/src/encryptedminutes.pdf',
        'errorExample.py':      'http://automatetheboringstuffwithpython.com/src/errorExample.py',
        'example.csv':          'http://automatetheboringstuffwithpython.com/src/example.csv',
        'example.zip':          'http://automatetheboringstuffwithpython.com/src/example.zip',
        'factorialLog.py':      'http://automatetheboringstuffwithpython.com/src/factorialLog.py',
        'formFiller.py':        'http://automatetheboringstuffwithpython.com/src/formFiller.py',
        'freezeExample.xlsx':   'http://automatetheboringstuffwithpython.com/src/freezeExample.xlsx',
        'getDocxText.py':       'http://automatetheboringstuffwithpython.com/src/getDocxText.py',
        'guessTheNumber.py':    'http://automatetheboringstuffwithpython.com/src/guessTheNumber.py',
        'guests.txt':           'http://automatetheboringstuffwithpython.com/src/guests.txt',
        'headings.docx':        'http://automatetheboringstuffwithpython.com/src/headings.docx',
        'hello.py':             'http://automatetheboringstuffwithpython.com/src/hello.py',
        'helloFunc.py':         'http://automatetheboringstuffwithpython.com/src/helloFunc.py',
        'helloFunc2.py':        'http://automatetheboringstuffwithpython.com/src/helloFunc2.py',
        'helloworld.docx':      'http://automatetheboringstuffwithpython.com/src/helloworld.docx',
        'inventory.py':         'http://automatetheboringstuffwithpython.com/src/inventory.py',
        'isPhoneNumber.py':     'http://automatetheboringstuffwithpython.com/src/isPhoneNumber.py',
        'lucky.py':             'http://automatetheboringstuffwithpython.com/src/lucky.py',
        'magic8ball.py':        'http://automatetheboringstuffwithpython.com/src/magic8ball.py',
        'magic8ball2.py':       'http://automatetheboringstuffwithpython.com/src/magic8ball2.py',
        'mapit.py':             'http://automatetheboringstuffwithpython.com/src/mapit.py',
        'mcb.pyw':              'http://automatetheboringstuffwithpython.com/src/mcb.pyw',
        'meetingminutes.pdf':   'http://automatetheboringstuffwithpython.com/src/meetingminutes.pdf',
        'meetingminutes2.pdf':  'http://automatetheboringstuffwithpython.com/src/meetingminutes2.pdf',
        'merged.xlsx':          'http://automatetheboringstuffwithpython.com/src/merged.xlsx',
        'morning-glory.jpg':    'http://automatetheboringstuffwithpython.com/src/morning-glory.jpg',
        'mouseNow.py':          'http://automatetheboringstuffwithpython.com/src/mouseNow.py',
        'mouseNow2.py':         'http://automatetheboringstuffwithpython.com/src/mouseNow2.py',
        'multidownloadxkcd.py': 'http://automatetheboringstuffwithpython.com/src/multidownloadxkcd.py',
        'multipleParagraphs.docx': 'http://automatetheboringstuffwithpython.com/src/multipleParagraphs.docx',
        'myPets.py':            'http://automatetheboringstuffwithpython.com/src/myPets.py',
        'passingReference.py':  'http://automatetheboringstuffwithpython.com/src/passingReference.py',
        'phoneandemail.py':     'http://automatetheboringstuffwithpython.com/src/phoneandemail.py',
        'picnicTable.py':       'http://automatetheboringstuffwithpython.com/src/picnicTable.py',
        'prettyCharacterCount.py': 'http://automatetheboringstuffwithpython.com/src/prettyCharacterCount.py',
        'produceSales.xlsx':    'http://automatetheboringstuffwithpython.com/src/produceSales.xlsx',
        'pw.py':                'http://automatetheboringstuffwithpython.com/src/pw.py',
        'quickweather.py':      'http://automatetheboringstuffwithpython.com/src/quickweather.py',
        'randomQuizGenerator.py': 'http://automatetheboringstuffwithpython.com/src/randomQuizGenerator.py',
        'readCensusExcel.py':   'http://automatetheboringstuffwithpython.com/src/readCensusExcel.py',
        'removeBorder.py':      'http://automatetheboringstuffwithpython.com/src/removeBorder.py',
        'removeCsvHeader.py':   'http://automatetheboringstuffwithpython.com/src/removeCsvHeader.py',
        'removeCsvHeader.zip':  'http://automatetheboringstuffwithpython.com/src/removeCsvHeader.zip',
        'renameDates.py':       'http://automatetheboringstuffwithpython.com/src/renameDates.py',
        'resizeAndAddLogo.py':  'http://automatetheboringstuffwithpython.com/src/resizeAndAddLogo.py',
        'restyled.docx':        'http://automatetheboringstuffwithpython.com/src/restyled.docx',
        'sameName.py':          'http://automatetheboringstuffwithpython.com/src/sameName.py',
        'sameName2.py':         'http://automatetheboringstuffwithpython.com/src/sameName2.py',
        'sameName3.py':         'http://automatetheboringstuffwithpython.com/src/sameName3.py',
        'sameName4.py':         'http://automatetheboringstuffwithpython.com/src/sameName4.py',
        'sampleChart.xlsx':     'http://automatetheboringstuffwithpython.com/src/sampleChart.xlsx',
        'sendDuesReminders.py': 'http://automatetheboringstuffwithpython.com/src/sendDuesReminders.py',
        'stopwatch.py':         'http://automatetheboringstuffwithpython.com/src/stopwatch.py',
        'styled.xlsx':          'http://automatetheboringstuffwithpython.com/src/styled.xlsx',
        'styles.xlsx':          'http://automatetheboringstuffwithpython.com/src/styles.xlsx',
        'textmyself.py':        'http://automatetheboringstuffwithpython.com/src/textmyself.py',
        'threadDemo.py':        'http://automatetheboringstuffwithpython.com/src/threadDemo.py',
        'tictactoe-example1.py': 'http://automatetheboringstuffwithpython.com/src/tictactoe-example1.py',
        'torrentStarter.py':    'http://automatetheboringstuffwithpython.com/src/torrentStarter.py',
        'twoPage.docx':         'http://automatetheboringstuffwithpython.com/src/twoPage.docx',
        'updateProduce.py':     'http://automatetheboringstuffwithpython.com/src/updateProduce.py',
        'updatedProduceSales.xlsx': 'http://automatetheboringstuffwithpython.com/src/updatedProduceSales.xlsx',
        'vampire.py':           'http://automatetheboringstuffwithpython.com/src/vampire.py',
        'watermark.pdf':        'http://automatetheboringstuffwithpython.com/src/watermark.pdf',
        'zeroDivide.py':        'http://automatetheboringstuffwithpython.com/src/zeroDivide.py',
        'zophie.png':           'http://automatetheboringstuffwithpython.com/src/zophie.png',

}


for k, v in URLS.items():
    print(TEMPLATE % (k, v))