var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length;i++) {
    updateBtns[i].addEventListener('click',function() {
        var productId = this.dataset.productos
        var action = this.dataset.action
        console.log('productId:',productId, 'Action:', action)
    })
}