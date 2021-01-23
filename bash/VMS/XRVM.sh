#/usr/bin/env bash


sudo cp ~/Downloads/iosxrv-demo-6.5.1.qcow2 /var/lib/libvirt/images/${2}.qcow2

sudo virt-install \
--name=${2} \
--description "${2}" \
--ram=3072 \
--vcpus=2 \
--boot hd,cdrom,menu=on \
--disk path=/var/lib/libvirt/images/${2}.qcow2,bus=ide,size=4 \
--import \
--graphic vnc \
--serial tcp,host=0.0.0.0:2251,mode=bind,protocol=telnet \
--network=bridge:br0,mac=52:54:00:01:01:00,model=virtio \
--network=bridge:br11,mac=52:54:00:01:01:01,model=virtio \
--network=bridge:br12,mac=52:54:00:01:01:02,model=virtio \
--network=bridge:br13,mac=52:54:00:01:01:03,model=virtio

