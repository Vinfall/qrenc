# QR encode

## Intro

Python script written in [Flask3](https://github.com/pallets/flask/) to generate QR code from input.
It works as a serverless function so you can deploy on serverless platforms like Vercel
or simply run it locally for better privacy.

Tested to work on Python 3.12.

## Usage

Let's say the instance is running at `qr.exmaple.com` (this example would not work),
your text is `helloworld`,
you can generate ics via `qr.example.com/hello world`.

No need to escape or modify anything, just put literal text as is.
It would (hopefully) deal with all your nonsense input.

## Shell function

You can also use it as a shell function, just like [qrenco.de](https://github.com/chubin/qrenco.de).
It's also why I write this script as the source code is not complete
and my fix just would invalidate this kind of use case.

First, adding this to your shell rc and reload via `exec zsh` or whatever:

```sh
qr() {
    curl --silent --get --data-urlencode "data=$1" "qr.example.com"
}
```

From now on, simply run `qr $1` to get the QR code:

```sh
$ qr "Across the Great Wall, we can reach every corner of the world."
██████████████    ██████    ██      ██    ████      ██████████████
██          ██        ████  ██    ██    ██          ██          ██
██  ██████  ██    ██████              ██  ████████  ██  ██████  ██
██  ██████  ██  ██  ████  ██      ██    ████    ██  ██  ██████  ██
██  ██████  ██  ██  ██  ██      ██    ████    ██    ██  ██████  ██
██          ██    ████      ██  ██████    ████  ██  ██          ██
██████████████  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██████████████
                  ██    ██    ████  ██          ██                
████      ██████  ████  ████      ██            ██      ████      
  ██    ████        ██    ██████  ████████  ████████  ████  ████  
  ████████████  ████  ██████████████    ████      ██      ██  ██  
                    ████      ████  ██                    ████████
  ██  ██  ██████  ████    ██████              ██████████          
    ██  ████      ████  ████  ████  ██████  ████    ████    ██  ██
            ████    ██    ██████                          ██  ██  
████████  ██    ██      ██████  ██    ████  ████    ██████  ██    
██    ██  ████  ██  ██  ██  ████  ██    ██  ██    ██  ████        
    ██  ██        ████        ██      ████    ██  ██  ██    ██████
██████  ████████  ██    ████████    ████  ██  ████  ████  ████  ██
██      ████          ██    ██  ██  ██  ██  ██  ██████    ████████
██  ████  ██████  ██  ██      ██  ████      ██  ████    ████      
████      ██    ██████  ████  ██    ████    ██████    ████████    
██    ██  ██████    ██    ██████    ██    ██    ██      ██  ████  
██            ████      ████        ██████  ██    ██  ██  ██████  
████  ████  ██      ████████    ██    ██        ████████████  ████
                ██████        ████████████      ██      ██        
██████████████  ██████████    ██  ██    ██    ████  ██  ██  ████  
██          ██  ████  ██                        ██      ██████    
██  ██████  ██    ██████      ██████        ██  ██████████    ████
██  ██████  ██    ██    ██████████  ████████    ████      ████████
██  ██████  ██      ████      ████    ████████    ██    ██  ██████
██          ██  ██████  ████        ██            ████      ██    
██████████████  ██████  ██  ████  ████        ████    ██      ██  
```

## [License](LICENSE)

BSD 3-Clause License
