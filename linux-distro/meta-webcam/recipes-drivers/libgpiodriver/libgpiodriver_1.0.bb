SUMMARY = "Driver-ish library for specific application management"
DESCRIPTION = "GPIO specific driver"

SECTION = "libs"
LICENSE = "GPLv2"
LIC_FILES_CHKSUM = "file://COPYING;md5=d41d8cd98f00b204e9800998ecf8427e"

SRC_URI = "file://libgpiodriver-1.0.tar.gz"

S = "${WORKDIR}/${PN}-${PV}"

EXTRA_OECONF += "--enable-shared"
inherit autotools

PROVIDES += "{PN}-staticdev"

FILES_${PN} = "${libdir}/*.so* ${bindir}/*"
#FILES_${PN}-staticdev = "${libdir}/*.a ${include_dir} ${datadir}"
