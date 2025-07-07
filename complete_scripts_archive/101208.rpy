label avg101208:
stop music

scene placeholderbackground
show sc004_01 2 as p12 at l(-12), light, zorder 6
window show
with fade_out
c121 '[textdict[1220680]]'
hide p12
show sc004_01 2 as p12 at l(-12), dark, zorder 6
show oc001_01 10 as p1 at r(-2), light, zorder 5
c13 '[textdict[1220681]]'
hide p12
hide p1
show oc001_01 10 as p1 at r(-2), dark, zorder 5
show sc004_01 1 as p12 at l(-12), light, zorder 6
c121 '[textdict[1220682]]'
menu:
    extend ""
    "[textdict[1220683]]":
        call avg101209
    "[textdict[1220684]]":
        call avg101210
    "[textdict[1220685]]":
        call avg101211
return