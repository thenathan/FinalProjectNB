#! /usr/bin/python

#creates .tre file to run in R

import pexpect

child = pexpect.spawn("mb -i test5.nex")
child.sendline(r"execute test5.nex")
child.sendline("sumt")
child.expect("MrBayes >")
print child.before
child.sendline("sump")
child.sendline("quit")

