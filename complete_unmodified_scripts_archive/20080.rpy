label avg20080(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc042_01 1', 'p49', [mid(-19), light], 6)
$ update_narrator('c493')
window show
with trans
get_char('c493') '[convertstrid(1004113)]' (**arg(1, 1004113))
menu:
    extend ""
    '[convertstrid(1004114)]':
        call avg0
    '[convertstrid(1004115)]':
        call avg0
    '[convertstrid(1004116)]':
        call avg0
return _return