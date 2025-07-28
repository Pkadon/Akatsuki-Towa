label avg29021:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1100007)]'
menu:
    extend ""
    "[textdict[1100008]]":
        call avg29022
    "[textdict[1100009]]":
        call avg29023
return