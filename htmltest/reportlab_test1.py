from reportlab.graphics.shapes import Drawing, String,PolyLine
from reportlab.graphics import renderPDF


d = Drawing(100, 100)
#s = String(50, 50, 'Hello, world!', textAnchor='middle')
s = PolyLine([(50, 50), (60, 50), (60, 60), (50, 60)])
d.add(s)
renderPDF.drawToFile(d, 'hello6.pdf', 'A simple PDF file')

#PolyLine([(0, 0), (10, 0), (10, 10), (0, 10)])

