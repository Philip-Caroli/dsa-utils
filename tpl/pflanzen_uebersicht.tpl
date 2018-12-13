<head>
    <title>DSA Datengrütze</title>
    <link rel="stylesheet" type="text/css" href="/static/style.css">
</head>
<body>
%for plant in plants:
<a href="/pflanze/{{plant['Name']}}">{{plant['Name']}}</a><br>
%end
</body>