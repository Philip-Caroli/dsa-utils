<head>
    <title>DSA Datengrütze</title>
    <link rel="stylesheet" type="text/css" href="/static/style.css">
</head>
<body>
%for key in plant:
<strong>{{key}}: </strong> {{plant[key]}} <br>
%end

<form action="/pflanzen">
    <input class="btn" type="submit" value="Zurück">
</form>

</body>