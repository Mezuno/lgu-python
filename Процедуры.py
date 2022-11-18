# При уч. Анастасии Самуйловой

# 1 ---------------------------

from graph import *
def treug(x, y, c):
brushColor(c)
polygon([(x,y),(x,y+60),
(x+100,y),(x,y)] )
penColor ( &quot;black&quot; )
treug ( 100, 160, &quot;blue&quot; )
treug ( 200, 100, &quot;green&quot; )
treug ( 200, 160, &quot;red&quot; )
run() - 3

# 2 ---------------------------

from graph import *
def treug(x, y, c):
brushColor(c)
polygon([(x,y),(x-30,y+60),
(x-60,y),(x,y)] )
penColor ( &quot;black&quot; )
treug ( 170, 100, &quot;blue&quot; )
treug ( 230, 100, &quot;green&quot; )
treug ( 200, 160, &quot;red&quot; )
run()
- 4

# 3 ---------------------------

from graph import *

def treug(x, y, c, d):
brushColor(c)

polygon([(x+d,y),(x+150-d,y),
(x+75,y-70),(x+d,y)] )

brushColor(&quot;brown&quot;)

polygon([(225,340),(235,150),(235,150),(250,340)])

penColor ( &quot;black&quot; )
treug ( 160, 270, &quot;green&quot;,20)
treug ( 160, 230, &quot;green&quot;,30)
treug ( 160, 190, &quot;green&quot;,40)
treug ( 160, 150, &quot;green&quot;,50)
treug ( 160, 110, &quot;green&quot;,60)
treug ( 160, 70, &quot;green&quot;,70)