label avg101904:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 6', 'p1', [r(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1218333)]'
$ update_portrait('oc001_01 6', 'p1', [r(-2), dark], 5)
$ update_portrait('sc011_01 5', 'p19', [l(-1), light, flip], 6)
c191 '[convertstrid(1218334)]'
$ update_portrait('sc011_01 5', 'p19', [l(-1), light, flip], 6)
c191 '[convertstrid(1218335)]'
menu:
    extend ""
    "[textdict[1218336]]":
        call avg101905
    "[textdict[1218337]]":
        call avg101906
    "[textdict[1218338]]":
        call avg101907
return