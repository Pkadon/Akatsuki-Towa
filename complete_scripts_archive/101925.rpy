label avg101925:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1218393)]'
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
$ update_portrait('sc011_01 2', 'p19', [l(-1), light, flip], 6)
c191 '[convertstrid(1218394)]'
$ update_portrait('sc011_01 2', 'p19', [l(-1), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1218395)]'
menu:
    extend ""
    "[textdict[1218396]]":
        call avg101926
    "[textdict[1218397]]":
        call avg101927
    "[textdict[1218398]]":
        call avg101928
return