# cipherHash
Custom Encryption Algrothim Used in IXO.js

# How to Install

```
npm i cipherHash
```

# How to Use
``` javascript
// Load the module
var c = require("cipherHash");

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

This is a super simple library that's made mainly for personal use, but feel free to use it!
