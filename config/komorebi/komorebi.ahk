#Requires AutoHotkey v2.0
#SingleInstance Force

Komorebic(cmd) {
    RunWait(format("komorebic.exe {}", cmd), , "Hide")
}

; Programs
#Enter::Run("powershell")
#+Enter::Run("http://color.aurlien.net/#72749e")
#v:: Run("code", "", "Hide")
#+e:: Run 'explorer.exe'
#e::
{
    Run "powershell -NoProfile yazi"
}


; Focus windows
#Left::Komorebic("focus left")
#Down::Komorebic("focus down")
#Up::Komorebic("focus up")
#Right::Komorebic("focus right")
#::Komorebic("focus-last-workspace")


; Toggle maximize
#f::Komorebic("toggle-maximize")

; Multiple monitor based
#p::Komorebic("cycle-monitor next")
#+p::Komorebic("cycle-move-to-monitor next")

; Close window
#+q::Komorebic("close")

; Move windows
#+Left::Komorebic("move left")
#+Down::Komorebic("move down")
#+Up::Komorebic("move up")
#+Right::Komorebic("move right")

; Workspaces
#1::Komorebic("focus-workspaces 0")  ; Rename to `focus-workspace` to have individual workspaces
#2::Komorebic("focus-workspaces 1")
#3::Komorebic("focus-workspaces 2")
#4::Komorebic("focus-workspaces 3")
#5::Komorebic("focus-workspaces 4")
#6::Komorebic("focus-workspaces 5")
#7::Komorebic("focus-workspaces 6")
#8::Komorebic("focus-workspaces 7")
#Tab::Komorebic("focus-last-workspace")

; Move windows across workspaces
#+1::Komorebic("move-to-workspace 0")
#+2::Komorebic("move-to-workspace 1")
#+3::Komorebic("move-to-workspace 2")
#+4::Komorebic("move-to-workspace 3")
#+5::Komorebic("move-to-workspace 4")
#+6::Komorebic("move-to-workspace 5")
#+7::Komorebic("move-to-workspace 6")
#+8::Komorebic("move-to-workspace 7")

