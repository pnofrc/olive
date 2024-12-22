
render = '''

<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>🫒</title>
    <meta name="description" content="ESTRATTO ASTRATTO DI INFOLIVE - computomanzia">
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

<body>
    <span id="start">CLICK PER PARTIRE</span>

    <div id="chain">
      '''

left = open('left.txt', 'r')
left_lines = left.readlines()


for line in left_lines:
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
    <div id="otherchain">'''


right = open('right.txt', 'r')
right_lines = right.readlines()


for line in right_lines:
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

    <!-- Steps Mono by Jean-Baptiste Morizot, Raphaël Bastide. Distributed by velvetyne.fr. -->
    <script src="script.js"> </script>

</body>

</html>'''


file = open('index.html', 'w')
file.write(render)
file.close()

