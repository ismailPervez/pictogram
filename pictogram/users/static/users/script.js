window.onload = () => {
    like_btns = document.querySelectorAll('.fa-heart')
    like_btns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            post_id = btn.dataset.id
            const likeTag = btn.parentElement.querySelector('.text')
            // console.log(likeTag.textContent)
            
            fetch('/like/post/' + post_id)
                .then(res => res.json())
                .then(data => {
                    if (data.status_code === 200) {
                        likeTag.textContent = parseInt(likeTag.textContent) + 1
                    }

                    else {
                        likeTag.textContent = parseInt(likeTag.textContent) - 1
                    }
                })
        })
    })
}