#/usr/bin/env bash


sudo cp ~/Downloads/cumulus-linux-4.1.1-vx-amd64-qemu.qcow2 /var/lib/libvirt/images/${1}.qcow2


sudo virt-install \
--name=${1} \
--description "${1} VM" \
--os-type=generic \
--ram=1024 \
--vcpus=1 \
--boot hd,cdrom,menu=on \
--disk path=/var/lib/libvirt/images/${1}.qcow2,bus=ide,size=4 \
--import \
--serial tcp,host=0.0.0.0:2252,mode=bind,protocol=telnet \
--network=bridge:br0,mac=52:54:00:03:01:00,model=virtio \
--network=bridge:br11,mac=52:54:00:03:01:01,model=virtio \
--network=bridge:br12,mac=52:54:00:03:01:02,model=virtio \
--network=bridge:br13,mac=52:54:00:03:01:03,model=virtio
