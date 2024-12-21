
render = '''

<!DOCTYPE html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]>      <html class="no-js"> <!--<![endif]-->
<html>

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>🫒</title>
    <meta name="description" content="">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="style.css">
    <script src="js/NoSleep.js"></script>
    <script src="js/jquery.js"></script>
    <script src="js/webpd-latest.js"></script>


    <script async>
        $(document).ready(function () {
            var patch
            $.get('./patch/ugoweb.pd', function (patchStr) {
                patch = Pd.loadPatch(patchStr)
            })
        });
    </script>
</head>

<body class="light">
    <div id="chain">
      '''

file = open('ok.txt', 'r')
lines = file.readlines()


for line in lines:
    if line != '':
        render += "<p>"
        words = line.split()
        for word in words:
            if word.lower().find("oliv") >= 0 or word.lower().find("uliv") >= 0:
                render += f'<span class="olive">{word} </span>'
            else:
                render += f'{word} '
        
        render += "</p>\n\n"



render += '''


  </div>

    <button id="theme">TOGGLE THEME</button>

    <!-- Steps Mono by Jean-Baptiste Morizot, Raphaël Bastide. Distributed by velvetyne.fr. -->
    <script src="script.js"> </script>

</body>

</html>'''


file = open('index2.html', 'w')
file.write(render)
file.close()

