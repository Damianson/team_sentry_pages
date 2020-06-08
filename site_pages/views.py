from site_pages.models import AddPage
from site_pages.serializers import PageSerializer, PageUpdateSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, RetrieveAPIView
import markdown
from rest_framework.response import Response
from rest_framework import status
class AddPageView(CreateAPIView):
    queryset = AddPage.objects.all()
    serializer_class = PageSerializer

class ListPageView(ListAPIView):
    queryset = AddPage.objects.all()
    serializer_class = PageSerializer 

class UpdatePageView(RetrieveUpdateAPIView):
    queryset = AddPage.objects.all()
    serializer_class = PageUpdateSerializer  

    

class PageContentView(RetrieveAPIView):
    queryset = AddPage.objects.all()
    serializer = PageSerializer

    def get(self, request, pk):
        try:
            page = AddPage.objects.get(pk=pk)
        except AddPage.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        title = page.title
        author = page.author
        description = page.description
        md = markdown.Markdown()
        content = md.convert(page.content)
        template = (f"""
<!doctype html>
<html lang='en'>
<head>
<meta charset='utf-8'>
<title>{title}</title>
<meta name='description' content='{description}'>
<meta name='author' content='{author}'>
<link rel='stylesheet' href='css/styles.css?v=1.0'>
</head>
<body>
{content}
<script src='js/scripts.js'>
</script>
</body>
</html>
""")
        data = {'html': template}
        return Response(data=data, status=status.HTTP_200_OK,)


# Create your views here.
