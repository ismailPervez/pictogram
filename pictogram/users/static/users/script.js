window.onload = () => {
    like_btns = document.querySelectorAll('.fa-heart')
    like_btns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            post_id = btn.dataset.id
            
            fetch('/like/post/' + post_id)
                .then(res => res.json())
                .then(data => console.log(data))
        })
    })
}