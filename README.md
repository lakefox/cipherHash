# cipherHash
Custom Encryption Algrothim

# How to Install

```
npm i cipherhash
```

# How to Use
``` javascript
// Load the module
var c = require("cipherhash");

// Encrypt a String

c.cipherHash("message", "password");

>>> "30A1Dd4XQawUdz"
  
// Decrypt a String

c.UnCipherHash("30A1Dd4XQawUdz", "password");

>>> "message"

// Get a Base64 Hash of a String

c.hash("string");

>>> "473287f8298dba7163a897908958f7c0eae733e25d2e027992ea2edc9bed2fa8"

```
