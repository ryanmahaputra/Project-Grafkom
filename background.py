from logging import lastResort
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random as rd
import os

def press_start():
    #P
    # glPushMatrix()
    glBegin(GL_POLYGON)
    glColor3ub(255, 255, 255)
    glVertex2f(114.025457746942, 120)
    glVertex2f(121.641991523289, 120)
    glVertex2f(121.641991523289, 148.05520792473)
    glVertex2f(114.025457746942, 148.05520792473)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(121.641991523289, 132.476834067432)
    glVertex2f(134.263701272602, 132.476834067432)
    glVertex2f(134.263701272602, 137.821676350254)
    glVertex2f(121.641991523289, 137.821676350254)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(121.641991523289, 142.900533975057)
    glVertex2f (134.263701272602, 142.900533975057)
    glVertex2f (134.263701272602, 148.05520792473)
    glVertex2f(121.641991523289, 148.05520792473)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(134.263701272602, 135.821676350254)
    glVertex2f(134.263701272602, 144.900533975057)
    glVertex2f(140.023931447772, 144.900533975057)
    glVertex2f(140.023931447772, 135.821676350254)
    glEnd()
     #R
    glPushMatrix()
    glTranslate(-215, 20, 0)
    glBegin(GL_POLYGON)
    glVertex2f(360, 100)
    glVertex2f(366.634961618039, 100)
    glVertex2f(366.634961618039, 128.178748246334)
    glVertex2f(360, 128.178748246334)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(366.634961618039, 128.178748246334)
    glVertex2f(366.634961618039, 121.192714293171)
    glVertex2f(378.047701653545, 121.192714293171)
    glVertex2f(378.047701653545, 128.178748246334)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(366.634961618039, 117.4920097772)
    glVertex2f(366.634961618039, 111.178074636055)
    glVertex2f(377.849175872605, 111.178074636055)
    glVertex2f(377.849175872605, 117.4920097772)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(382.74774474328, 123.059709769269)
    glVertex2f(382.74774474328, 116.285093245945)
    glVertex2f(375.556228741651, 116.285093245945)
    glVertex2f(375.556228741651, 123.059709769269)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(377.849175872605, 111.178074636055)
    glVertex2f(370.816515026117, 111.178074636055)
    glVertex2f(370.816515026117, 106.54651054885)
    glVertex2f(377.849175872605, 106.54651054885)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(382.74774474328, 106.54651054885)
    glVertex2f(382.74774474328, 100)
    glVertex2f(375.556228741651, 100)
    glVertex2f(375.556228741651, 106.54651054885)
    glEnd()
    glPopMatrix()
    #E
    glPushMatrix()
    glTranslate(-43, 20, 0)
    glBegin(GL_POLYGON)
    glVertex2f(215.985715419604, 100)
    glVertex2f(222.974547970252, 100)
    glVertex2f(222.974547970252, 128.088899942189)
    glVertex2f(215.985715419604, 128.088899942189)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(215.985715419604, 100)
    glVertex2f(232.690729808959, 100)
    glVertex2f(232.690729808959, 106.916068671038)
    glVertex2f(215.985715419604, 106.916068671038)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(232.690729808959, 111.688929925175)
    glVertex2f(232.690729808959, 117.314087831836)
    glVertex2f(215.985715419604, 117.314087831836)
    glVertex2f(215.985715419604, 111.688929925175)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(232.690729808959, 121.234652433448)
    glVertex2f(232.690729808959, 128.088899942189)
    glVertex2f(215.985715419604, 128.088899942189)
    glVertex2f(215.985715419604, 121.234652433448)
    glEnd()
    glPopMatrix()
    #S
    glPushMatrix()
    glTranslate(-23, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(218.409132952884, 120)
    glVertex2f(240.920848376541, 120)
    glVertex2f(240.920848376541, 126.921615421501)
    glVertex2f(218.409132952884, 126.921615421501)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(240.920848376541, 120)
    glVertex2f(235.749238076512, 120)
    glVertex2f(235.749238076512, 137.785897874598)
    glVertex2f(240.920848376541, 137.785897874598)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(240.920848376541, 137.785897874598)
    glVertex2f(240.920848376541, 132.54487854266)
    glVertex2f(218.409132952884, 132.54487854266)
    glVertex2f(218.409132952884, 137.785897874598)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(218.409132952884, 136.54487854266)
    glVertex2f(224.189167994093, 136.54487854266)
    glVertex2f(224.189167994093, 148.05520792473)
    glVertex2f(218.409132952884, 148.05520792473)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(218.409132952884, 148.443692011965)
    glVertex2f(240.920848376541, 148.443692011965)
    glVertex2f(240.920848376541, 143.05520792473)
    glVertex2f(218.409132952884, 143.05520792473)
    glEnd()
    glPopMatrix()
    #S
    glPushMatrix()
    glTranslate(5, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(218.409132952884, 120)
    glVertex2f(240.920848376541, 120)
    glVertex2f(240.920848376541, 126.921615421501)
    glVertex2f(218.409132952884, 126.921615421501)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(240.920848376541, 120)
    glVertex2f(235.749238076512, 120)
    glVertex2f(235.749238076512, 137.785897874598)
    glVertex2f(240.920848376541, 137.785897874598)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(240.920848376541, 137.785897874598)
    glVertex2f(240.920848376541, 132.54487854266)
    glVertex2f(218.409132952884, 132.54487854266)
    glVertex2f(218.409132952884, 137.785897874598)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(218.409132952884, 136.54487854266)
    glVertex2f(224.189167994093, 136.54487854266)
    glVertex2f(224.189167994093, 148.05520792473)
    glVertex2f(218.409132952884, 148.05520792473)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(218.409132952884, 148.443692011965)
    glVertex2f(240.920848376541, 148.443692011965)
    glVertex2f(240.920848376541, 143.05520792473)
    glVertex2f(218.409132952884, 143.05520792473)
    glEnd()
    glPopMatrix()
    #S
    glPushMatrix()
    glTranslate(50, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(218.409132952884, 120)
    glVertex2f(240.920848376541, 120)
    glVertex2f(240.920848376541, 126.921615421501)
    glVertex2f(218.409132952884, 126.921615421501)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(240.920848376541, 120)
    glVertex2f(235.749238076512, 120)
    glVertex2f(235.749238076512, 137.785897874598)
    glVertex2f(240.920848376541, 137.785897874598)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(240.920848376541, 137.785897874598)
    glVertex2f(240.920848376541, 132.54487854266)
    glVertex2f(218.409132952884, 132.54487854266)
    glVertex2f(218.409132952884, 137.785897874598)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(218.409132952884, 136.54487854266)
    glVertex2f(224.189167994093, 136.54487854266)
    glVertex2f(224.189167994093, 148.05520792473)
    glVertex2f(218.409132952884, 148.05520792473)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(218.409132952884, 148.443692011965)
    glVertex2f(240.920848376541, 148.443692011965)
    glVertex2f(240.920848376541, 143.05520792473)
    glVertex2f(218.409132952884, 143.05520792473)
    glEnd()
    glPopMatrix()
    #T
    glPushMatrix()
    glTranslate(-4, 0, 0)
    glBegin(GL_POLYGON) 
    glVertex2f(311.520095186385, 120)
    glVertex2f(317.286445329016, 120)
    glVertex2f(317.286445329016, 148.443692011965)
    glVertex2f(311.520095186385, 148.443692011965)
    glEnd()
    glBegin(GL_POLYGON) 
    glVertex2f(301.667005315297, 148.443692011965)
    glVertex2f(301.667005315297, 143.05520792473)
    glVertex2f(326.708455128207, 143.05520792473)
    glVertex2f(326.708455128207, 148.443692011965)
    glEnd()     
    glPopMatrix() 
    #A
    glPushMatrix()
    glTranslate(183, 20, 0)
    glBegin(GL_POLYGON)
    glVertex2f(152.086998925403, 128.088899942189)
    glVertex2f(163.956272983872, 128.088899942189)
    glVertex2f(163.956272983872, 121.484363125437)
    glVertex2f(152.086998925403, 121.484363125437)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(169.022426545413, 123.221330060836)
    glVertex2f(169.022426545413, 100)
    glVertex2f(162.07455880387, 100)
    glVertex2f(162.07455880387, 123.221330060836)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(152.656826642228, 123.221330060836)
    glVertex2f(152.656826642228, 100)
    glVertex2f(146.03765493159, 100)
    glVertex2f(146.03765493159, 123.221330060836)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(152.656826642228, 117.303249239171)
    glVertex2f(152.656826642228, 111.586691852668)
    glVertex2f(162.07455880387, 111.586691852668)
    glVertex2f(162.07455880387, 117.303249239171)
    glEnd()  
    glPopMatrix()
     #R
    glPushMatrix()
    glTranslate(-2, 20, 0)
    glBegin(GL_POLYGON)
    glVertex2f(360, 100)
    glVertex2f(366.634961618039, 100)
    glVertex2f(366.634961618039, 128.178748246334)
    glVertex2f(360, 128.178748246334)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(366.634961618039, 128.178748246334)
    glVertex2f(366.634961618039, 121.192714293171)
    glVertex2f(378.047701653545, 121.192714293171)
    glVertex2f(378.047701653545, 128.178748246334)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(366.634961618039, 117.4920097772)
    glVertex2f(366.634961618039, 111.178074636055)
    glVertex2f(377.849175872605, 111.178074636055)
    glVertex2f(377.849175872605, 117.4920097772)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(382.74774474328, 123.059709769269)
    glVertex2f(382.74774474328, 116.285093245945)
    glVertex2f(375.556228741651, 116.285093245945)
    glVertex2f(375.556228741651, 123.059709769269)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(377.849175872605, 111.178074636055)
    glVertex2f(370.816515026117, 111.178074636055)
    glVertex2f(370.816515026117, 106.54651054885)
    glVertex2f(377.849175872605, 106.54651054885)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(382.74774474328, 106.54651054885)
    glVertex2f(382.74774474328, 100)
    glVertex2f(375.556228741651, 100)
    glVertex2f(375.556228741651, 106.54651054885)
    glEnd()
    glPopMatrix()
    #T
    glPushMatrix()
    glTranslate(85, 0, 0)
    glBegin(GL_POLYGON) 
    glVertex2f(311.520095186385, 120)
    glVertex2f(317.286445329016, 120)
    glVertex2f(317.286445329016, 148.443692011965)
    glVertex2f(311.520095186385, 148.443692011965)
    glEnd()
    glBegin(GL_POLYGON) 
    glVertex2f(301.667005315297, 148.443692011965)
    glVertex2f(301.667005315297, 143.05520792473)
    glVertex2f(326.708455128207, 143.05520792473)
    glVertex2f(326.708455128207, 148.443692011965)
    glEnd()     
    glPopMatrix() 


def background_1():
    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 51)
    glVertex2f(0,500)
    glVertex2f(500,500)
    glVertex2f(500,0)
    glVertex2f(0,0)
    glEnd()
    
def GAMEOVER():
    glPushMatrix()
    glTranslate(20, 20, 0)
    #G
    glBegin(GL_POLYGON)
    glColor3ub(163, 12, 2)
    glVertex2f(120.217318891938, 128.088899942189)
    glVertex2f(136.93873391162, 128.088899942189)
    glVertex2f(136.93873391162, 120.964983484048)
    glVertex2f(120.217318891938, 120.964983484048)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(114.188388073652, 123.237216685859)
    glVertex2f(114.188388073652, 106.559749809806)
    glVertex2f(121.554269277188, 106.559749809806)
    glVertex2f(121.554269277188, 123.237216685859)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(120, 100)
    glVertex2f(131.838707184011, 100)
    glVertex2f(131.838707184011, 106.559749809806)
    glVertex2f(120,106.559749809806)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(137.258883918688, 105.725876466004)
    glVertex2f(137.258883918688, 117.261124388607)
    glVertex2f(129.893002715152, 117.261124388607)
    glVertex2f(129.893002715152, 105.725876466004)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(137.258883918688, 117.261124388607)
    glVertex2f(125.028741543006, 117.261124388607)
    glVertex2f(125.028741543006, 111.007074310087)
    glVertex2f(137.258883918688, 111.007074310087)
    glEnd()
    #A
    glBegin(GL_POLYGON)
    glVertex2f(152.086998925403, 128.088899942189)
    glVertex2f(163.956272983872, 128.088899942189)
    glVertex2f(163.956272983872, 121.484363125437)
    glVertex2f(152.086998925403, 121.484363125437)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(169.022426545413, 123.221330060836)
    glVertex2f(169.022426545413, 100)
    glVertex2f(162.07455880387, 100)
    glVertex2f(162.07455880387, 123.221330060836)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(152.656826642228, 123.221330060836)
    glVertex2f(152.656826642228, 100)
    glVertex2f(146.03765493159, 100)
    glVertex2f(146.03765493159, 123.221330060836)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(152.656826642228, 117.303249239171)
    glVertex2f(152.656826642228, 111.586691852668)
    glVertex2f(162.07455880387, 111.586691852668)
    glVertex2f(162.07455880387, 117.303249239171)
    glEnd()
    #m
    glBegin(GL_POLYGON)
    glVertex2f(177.884555835418, 128.088899942189)
    glVertex2f(177.884555835418, 100)
    glVertex2f(185.015817743225, 100)
    glVertex2f(185.015817743225, 128.088899942189)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(185.015817743225, 122.819965433085)
    glVertex2f(185.015817743225, 116.452767301067)
    glVertex2f(190.61895209936,  116.452767301067)
    glVertex2f(190.61895209936,  122.819965433085)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(189.090824547687, 111.359008795453)
    glVertex2f(195.203334754378, 111.359008795453)
    glVertex2f(195.203334754378, 117.34417503955)
    glVertex2f(189.090824547687, 117.34417503955)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(200, 100)
    glVertex2f(207.100876521511, 100)
    glVertex2f(207.100876521511, 128.088899942189)
    glVertex2f(200, 128.088899942189)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(200, 116.452767301067)
    glVertex2f(200, 122.819965433085)
    glVertex2f(193.967457735109, 122.819965433085)
    glVertex2f(193.967457735109, 116.452767301067)
    glEnd()
    #E
    glBegin(GL_POLYGON)
    glVertex2f(215.985715419604, 100)
    glVertex2f(222.974547970252, 100)
    glVertex2f(222.974547970252, 128.088899942189)
    glVertex2f(215.985715419604, 128.088899942189)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(215.985715419604, 100)
    glVertex2f(232.690729808959, 100)
    glVertex2f(232.690729808959, 106.916068671038)
    glVertex2f(215.985715419604, 106.916068671038)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(232.690729808959, 111.688929925175)
    glVertex2f(232.690729808959, 117.314087831836)
    glVertex2f(215.985715419604, 117.314087831836)
    glVertex2f(215.985715419604, 111.688929925175)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(232.690729808959, 121.234652433448)
    glVertex2f(232.690729808959, 128.088899942189)
    glVertex2f(215.985715419604, 128.088899942189)
    glVertex2f(215.985715419604, 121.234652433448)
    glEnd()
    #O
    glBegin(GL_POLYGON)
    glVertex2f(269.199454196716, 128.088899942189)
    glVertex2f(281.464511891195, 128.088899942189)
    glVertex2f(281.464511891195, 120.902207121357)
    glVertex2f(269.199454196716, 120.902207121357)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(269.199454196716, 100)
    glVertex2f(281.464511891195, 100)
    glVertex2f(281.464511891195, 107.450805158463)
    glVertex2f(269.199454196716, 107.450805158463)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(286.699597492497, 122.098798115949)
    glVertex2f(286.699597492497, 106.393645422081)
    glVertex2f(279.819199273643, 106.393645422081)
    glVertex2f(279.819199273643, 122.098798115949)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(271.143914562914, 122.098798115949)
    glVertex2f(271.143914562914, 106.393645422081)
    glVertex2f(263.863918053971, 106.393645422081)
    glVertex2f(263.863918053971, 122.098798115949)
    glEnd()
    #V
    glBegin(GL_POLYGON)
    glVertex2f(295.736509966406, 128.088899942189)
    glVertex2f(302.939587645871, 128.088899942189)
    glVertex2f(302.939587645871, 116.122763182273)
    glVertex2f(295.736509966406, 116.122763182273)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(317.860248553335, 128.088899942189)
    glVertex2f(324.720322533778, 128.088899942189)
    glVertex2f(324.720322533778, 116.122763182273)
    glVertex2f(317.860248553335, 116.122763182273)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(311.631879198328, 116.920612785298)
    glVertex2f(319.124672968599, 116.920612785298)
    glVertex2f(319.124672968599, 106.147058289705)
    glVertex2f(311.631879198328, 106.147058289705)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(300.782778270511, 116.920612785298)
    glVertex2f(307.895691439577, 116.920612785298)
    glVertex2f(307.895691439577, 106.147058289705)
    glVertex2f(300.782778270511, 106.147058289705)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(313.649547874026, 100)
    glVertex2f(313.649547874026, 107.499162933983)
    glVertex2f(306.426312757819, 107.499162933983)
    glVertex2f(306.426312757819, 100)
    glEnd()
    #E
    glBegin(GL_POLYGON)
    glVertex2f(334.188319033393, 100)
    glVertex2f(339.851112679232, 100)
    glVertex2f(339.851112679232, 128.088899942189)
    glVertex2f(334.188319033393, 128.088899942189)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(334.188319033393, 100)
    glVertex2f(351.071833421914, 100)
    glVertex2f(351.071833421914, 106.916068671038)
    glVertex2f(334.188319033393, 106.916068671038)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(351.071833421914, 111.688929925175)
    glVertex2f(351.071833421914, 117.314087831836)
    glVertex2f(334.188319033393, 117.314087831836)
    glVertex2f(334.188319033393, 111.688929925175)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(351.071833421914, 121.234652433448)
    glVertex2f(351.071833421914, 128.088899942189)
    glVertex2f(334.188319033393, 128.088899942189)
    glVertex2f(334.188319033393, 121.234652433448)
    glEnd()
    #R
    glBegin(GL_POLYGON)
    glVertex2f(360, 100)
    glVertex2f(366.634961618039, 100)
    glVertex2f(366.634961618039, 128.178748246334)
    glVertex2f(360, 128.178748246334)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(366.634961618039, 128.178748246334)
    glVertex2f(366.634961618039, 121.192714293171)
    glVertex2f(378.047701653545, 121.192714293171)
    glVertex2f(378.047701653545, 128.178748246334)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(366.634961618039, 117.4920097772)
    glVertex2f(366.634961618039, 111.178074636055)
    glVertex2f(377.849175872605, 111.178074636055)
    glVertex2f(377.849175872605, 117.4920097772)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(382.74774474328, 123.059709769269)
    glVertex2f(382.74774474328, 116.285093245945)
    glVertex2f(375.556228741651, 116.285093245945)
    glVertex2f(375.556228741651, 123.059709769269)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(377.849175872605, 111.178074636055)
    glVertex2f(370.816515026117, 111.178074636055)
    glVertex2f(370.816515026117, 106.54651054885)
    glVertex2f(377.849175872605, 106.54651054885)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(382.74774474328, 106.54651054885)
    glVertex2f(382.74774474328, 100)
    glVertex2f(375.556228741651, 100)
    glVertex2f(375.556228741651, 106.54651054885)
    glEnd()
    glPopMatrix()

def youwin():
    glPushMatrix()
    glTranslate(-10, 20, 0)
    #Huruf Y
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(80,140)
    glEnd()

    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(80,130)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(80, 120)
    glEnd()

    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(90,140)
    glEnd()

    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(90,130)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(90, 120)
    glEnd()

    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(90, 110)
    glEnd()

    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(100, 110)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(110, 110)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(120, 110)
    glEnd()

    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(120,140)
    glEnd()

    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(120,130)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(120, 120)
    glEnd()

    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(120, 110)
    glEnd()

    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(130,140)
    glEnd()

    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(130,130)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(130, 120)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(100,100)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(100,90)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(100,80)
    glEnd()

    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(110,100)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(110,90)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(110, 80)
    glEnd()

    #huruf O
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(145, 120)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(145, 110)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(145, 100)
    glEnd()

    #s
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(155, 130)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(155, 120)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(155, 110)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(155, 100)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(155, 90)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(165, 130)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(165, 140)
    glEnd()

    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(165, 90)
    glEnd()

    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(165, 80)
    glEnd()

    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(175, 80)
    glEnd()


    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(185, 80)
    glEnd()

    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(195, 80)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(195, 90)
    glEnd()

    #dd
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(165, 140)
    glEnd()

    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(175, 140)
    glEnd()


    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(185, 140)
    glEnd()

    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(195, 140)
    glEnd()

    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(195, 130)
    glEnd()

    #s
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(205, 130)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(205, 120)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(205, 110)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(205, 100)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(205, 90)
    glEnd()
    
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(215, 120)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(215, 110)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(215, 100)
    glEnd()

    #huruf U
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(230, 140)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(230, 130)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(230, 120)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(230, 110)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(230, 100)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(230, 90)
    glEnd()
    #sa
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(240, 140)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(240, 130)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(240, 120)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(240, 110)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(240, 100)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(240, 90)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(250, 90)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(250, 80)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(240, 80)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(260, 80)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(270, 80)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(270, 90)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(280, 90)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(280, 140)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(280, 130)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(280, 120)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(280, 110)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(280, 100)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(280, 90)
    glEnd()

    #huruf W
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(295, 140)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(295, 130)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(305, 140)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(305, 130)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(305, 120)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(305, 110)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(305, 100)
    glEnd()
    #ff
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(315, 120)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(315, 110)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(315, 100)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(315, 90)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(315, 80)
    glEnd()
    #d
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(325, 100)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(325, 90)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(325, 80)
    glEnd()

    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(335, 140)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(335, 130)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(335, 120)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(335, 110)
    glEnd()

    #dd
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(345, 140)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(345, 130)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(345, 120)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(345, 110)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(345, 100)
    glEnd()
    #dsf
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(355, 100)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(355, 90)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(355, 80)
    glEnd()
    #hd
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(365, 120)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(365, 110)
    glEnd()   
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(365, 100)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(365, 90)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(365, 80)
    glEnd()


    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(375, 140)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(375, 130)
    glEnd()    
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(375, 120)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(375, 110)
    glEnd() 

    #huruf I
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(390, 140)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(390, 130)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(390, 120)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(390, 110)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(390, 100)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(390, 90)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(390, 80)
    glEnd()
    #jg
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(400, 140)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(400, 130)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(400, 120)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(400, 110)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(400, 100)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(400, 90)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(400, 80)
    glEnd()

    #Huruf N
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(415, 140)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(415, 130)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(415, 120)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(415, 110)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(415, 100)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(415, 90)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(415, 80)
    glEnd()

    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(425, 130)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(425, 120)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(425, 110)
    glEnd()

    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(435, 120)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(435, 110)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(435, 100)
    glEnd()

    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(445, 140)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(445, 130)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(445, 120)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(445, 110)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(445, 100)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(445, 90)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glPointSize(20.0)
    glBegin(GL_POINTS)
    glVertex2f(445, 80)
    glEnd()
    glPopMatrix()


