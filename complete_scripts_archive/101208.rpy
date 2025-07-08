label avg101208:
stop music

scene placeholderbackground
$ update_portrait('sc004_01 2', 'p12', [l(-12), light, flip], 6)
window show
with fade_in
c121 '[textdict[1220680]]'
hide p12
$ update_portrait('sc004_01 2', 'p12', [l(-12), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1220681]]'
hide p12
hide p1
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc004_01 1', 'p12', [l(-12), light, flip], 6)
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