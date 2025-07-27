label avg101221:

stop music
scene placeholderbackground
$ update_portrait('sc004_01 4', 'p12', [l(-12), light, flip], 6)
$ update_narrator('c121')
window show
with fade_in
c121 '[convertstrid(1220719)]'
$ update_portrait('sc004_01 4', 'p12', [l(-12), dark, flip], 6)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1220720)]'
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc004_01 3', 'p12', [l(-12), light, flip], 6)
c121 '[convertstrid(1220721)]'
$ update_portrait('sc004_01 3', 'p12', [l(-12), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1220722)]'
menu:
    extend ""
    "[textdict[1220723]]":
        call avg101222
    "[textdict[1220724]]":
        call avg101223
    "[textdict[1220725]]":
        call avg101224
return