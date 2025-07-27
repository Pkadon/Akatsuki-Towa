label avg20117:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1005536)]'
menu:
    extend ""
    "[textdict[1005537]]":
        call avg10100
    "[textdict[1005538]]":
        call avg10101
return