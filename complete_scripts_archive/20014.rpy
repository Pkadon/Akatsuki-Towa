label avg20014:

play music "ED6518.ogg"
scene avg_bg_014
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1000941)]'
hide p1
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 6)
c23 '[convertstrid(1000942)]'
hide p2
c5173 '[convertstrid(1000943)]'
c5173 '[convertstrid(1000944)]'
c5173 '[convertstrid(1000945)]'
menu:
    extend ""
    "[textdict[1000946]]":
        call avg20015
    "[textdict[1000947]]":
        call avg20016
return