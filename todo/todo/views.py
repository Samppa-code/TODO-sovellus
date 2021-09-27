from django.http import  HttpResponse

from .models import Tehtava


ETUSIVU_HTML = """
<html>
<body>
<h1>Tehtävät</h1>
Tekemattä : <br>
{}
</body>
</html>
"""


def etusivu(request):
    tehtavalinkit = []
    for tehtava in Tehtava.objects.all():
        linkki ='<a href="/Tehtava/{id}/">{tehtava}</a>'.format(
            id = tehtava.id,
            tehtava = tehtava.tehtava
        )
         
        tehtavalinkit.append(linkki)
    linkkiteksti = '<br>'.join(tehtavalinkit)
    return HttpResponse(ETUSIVU_HTML.format(linkkiteksti))



def tehtavasivu(request, tehtava_id):
    tehtavat= Tehtava.objects.filter(id=tehtava_id)
    tehtava = tehtavat.get()
    return HttpResponse(TEHTAVASIVU_HTML.format(
        nimi = tehtava.nimi,
    ))


TEHTAVASIVU_HTML = """
<html>
<body>
<h1>Tehtavat</h1>
<h2>{tehtava}</h2>
<p>
<a href="/">[etusivu]</a>
</p>
</body>
</html>
"""