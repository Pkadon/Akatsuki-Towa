label avg101208:
stop music

stop music
scene placeholderbackground
with fade
show sc004_01 2 as c12portrait at leftside(-12), zorder 5
c121 '[textdict[1220680]]'
stop music
hide c12portrait
show sc004_01 2 as c12portrait at darkleft(-12), zorder 6
show oc001_01 10 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[1220681]]'
stop music
hide c12portrait
hide c1portrait
show oc001_01 10 as c1portrait at darkright(-2), zorder 5
show sc004_01 1 as c12portrait at leftside(-12), zorder 5
c121 '[textdict[1220682]]'
menu:
    "[textdict[1220683]]":
        call avg101209
    "[textdict[1220684]]":
        call avg101210
    "[textdict[1220685]]":
        call avg101211
return