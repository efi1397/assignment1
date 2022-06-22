echo "Install virutal machine"

vagrant up

[system.Diagnostics.Process]::Start("chrome","http://localhost/")
