label avg101809(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc010_01 1', 'p18', [l(-10), light, flip], 6)
$ update_narrator('c181')
window show
with trans
get_char('c181') '[convertstrid(1222182)]' (**arg(1, 1222182))
return "avg101809"