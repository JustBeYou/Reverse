break *0x4012A7
r 123456

set logging on
set logging file output.log
set $i = 0
set $j = 0

while $i < 10
    while $j < 41
        p/x $al
        set $j = $j + 1
        c
    end

    set $i = $i + 1
    set $j = 0
end
