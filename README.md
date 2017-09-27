# Eos: Verifiable elections

Work in progress – current development is focusing on an API for elections and cryptography, future work will be directed towards a functional user interface

## Comparison with competitors

| | Helios | Eos
--- | --- | ---
Usable | Yes | No
Good | Yes | No
Eye Candy | No | Heck No

## Cryptographic details and references

Eos aims to be implementation-agnostic with respect to cryptographic details. The included *eos.psr* package provides an example implementation with the following particulars:

* ElGamal encryption
  * MENEZES, Alfred J., VAN OORSCHOT, Paul C. and VANSTONE, Scott A. *Handbook of Applied Cryptography*. CRC Press, 2001. Fifth printing. ISBN 978-0-8493-8523-0. Available from: http://cacr.uwaterloo.ca/hac/.
* Distributed threshold ElGamal due to **P**edersen (1991) – planned
* **S**igned ElGamal due to Seurin and Treger (2013)
* **R**andomised partial checking (RPC) due to Jakobsson, Juels and Rivest (2002)

## Mega disclaimer

This is a fun side-project of mine, and should in no way be considered to be a serious attempt to build a production-ready election system suitable for real world deployment. Not even crypto experts are quite up to the task, and I am most certainly not a crypto expert, nor am I anything resembling a professional in any field even tangentially related to cryptographic elections.

I cannot guarantee the security of this implementation whatsoever. In fact, I would go so far as to guarantee that this software has so many holes it gives Swiss cheese a run for its money. That said, please feel free to roast Eos on the issue tracker!
