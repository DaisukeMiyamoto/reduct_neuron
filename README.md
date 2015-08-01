# reduct_neuron
reduce branch of neuron (swc file)

## basic usage
### load swc and show histgram
    from swc import Swc
    swc = Swc(filename='hogehoge.swc')
    swc.show_filename()
    swc.show_hist()

### options
* add compartment fingerprint to second field of SWC  
`swc = Swc(filename='hogehoge.swc', set_fingerprint=1)`

## reduct compartment
