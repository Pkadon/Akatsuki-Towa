label avg101908:

stop music
scene placeholderbackground
$ update_portrait('sc011_01 4', 'p19', [l(-1), light, flip], 6)
$ update_narrator('c191')
window show
with fade_in
c191 '[convertstrid(1218343)]'
$ update_portrait('sc011_01 4', 'p19', [l(-1), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1218344)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc011_01 2', 'p19', [l(-1), light, flip], 6)
c191 '[convertstrid(1218345)]'
menu:
    extend ""
    "[textdict[1218346]]":
        call avg101909
    "[textdict[1218347]]":
        call avg101910
    "[textdict[1218348]]":
        call avg101911
return