import sys
import random

from binascii import hexlify, unhexlify
from Crypto.Cipher import DES3

# Based on
# https://www.ibm.com/support/knowledgecenter/en/SSLTBW_2.1.0/com.ibm.zos.v2r1.csfb400/csfb4za2598.htm

def histogram(pvv_pins):
    h = {}
    for k, v in pvv_pins.items():
        try:
            h[len(v)] += 1
        except KeyError:
            h[len(v)] = 1
    return sorted(h.items(), key=lambda x: x[0])

def extract_pvv(hexstring):
    pvv = ''
   
    for c in hexstring:
        try:
            int(c)
            pvv += str(int(c, 16))
            if len(pvv) == 4:
              return pvv
        except ValueError:
            continue
    
    for c in hexstring:
        try:
            int(c)
        except ValueError:
            pvv += str(int(c, 16) - 10)
            if len(pvv) == 4:
                return pvv

def main():
    random.seed()

    pvki = '1'
    pvk = '%032X' % random.getrandbits(8 * 8 * 2)

    print 'Using random PIN Verification Key %s with Index %s' % (pvk, pvki)

    # PVV Generation Key Left and Right
    pgkl = DES3.new(pvk[:16], DES3.MODE_ECB)
    pgkr = DES3.new(pvk[16:], DES3.MODE_ECB)

    while True:
        # Ignore Luhn check digit, it is not used by the algorithm
        pan = str(random.randrange(4112980000000000, 4112989999999999))

        pvv_pins = {}
        for i in xrange(10000):
            pin = '%04d' % i

            # Transformed Security Parameter 11 + 1 + 4
            tsp = unhexlify(pan[-12:-1] + pvki + pin)

            encipherment_result = pgkl.encrypt(pgkr.decrypt((pgkl.encrypt(tsp))))
            hexstring = hexlify(encipherment_result).upper()
            pvv = extract_pvv(hexstring)

            try:
                pvv_pins[pvv].append(pin)
            except KeyError:
                pvv_pins[pvv] = [pin]

        top_collision = sorted(pvv_pins.items(), key=lambda x: len(x[1]), reverse=True)[0]
        print 'PAN %s has %d unique PVVs; PINs %r => PVV %r' % (pan, len(pvv_pins), top_collision[1], top_collision[0])
        print '\tPVV Histogram: { %s }' % (', '.join(['%s: %s' % (k, v) for k, v in histogram(pvv_pins)]))
#        if len(top_collision[1]) > 8: break

if __name__ == '__main__':
    main()
