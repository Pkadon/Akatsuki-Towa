label avg101621:

stop music
scene placeholderbackground
$ update_portrait('sc008_01 3', 'p16', [l(-18), light, flip], 6)
$ update_narrator('c161')
window show
with fade_in
c161 '[convertstrid(1221586)]'
$ update_portrait('sc008_01 3', 'p16', [l(-18), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1221587)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc008_01 1', 'p16', [l(-18), light, flip], 6)
c161 '[convertstrid(1221588)]'
menu:
    extend ""
    "[textdict[1221589]]":
        call avg101622
    "[textdict[1221590]]":
        call avg101623
    "[textdict[1221591]]":
        call avg101624
return