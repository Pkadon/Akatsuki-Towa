label avg101921:
stop music

scene placeholderbackground
$ update_portrait('sc011_01 2', 'p19', [l(-1), light, flip], 6)
window show
with fade_in
c191 '[textdict[1218383]]'
$ update_portrait('sc011_01 2', 'p19', [l(-1), dark, flip], 6)
$ update_portrait('oc001_01 23', 'p1', [r(-2), light], 5)
c13 '[textdict[1218384]]'
$ update_portrait('oc001_01 23', 'p1', [r(-2), dark], 5)
$ update_portrait('sc011_01 4', 'p19', [l(-1), light, flip], 6)
c191 '[textdict[1218385]]'
menu:
    extend ""
    "[textdict[1218386]]":
        call avg101922
    "[textdict[1218387]]":
        call avg101923
    "[textdict[1218388]]":
        call avg101924
return