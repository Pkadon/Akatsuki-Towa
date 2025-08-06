label avg20014:

play music "ED6518.ogg"
scene avg_bg_008
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1000941)]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), l_shake, light, flip], 6)
c21 '[convertstrid(1000942)]'
hide p2
c5171 '[convertstrid(1000943)]'
c5171 '[convertstrid(1000944)]'
c5171 '[convertstrid(1000945)]'
menu:
    extend ""
    "[textdict[1000946]]":
        call avg20015
    "[textdict[1000947]]":
        call avg20016
return