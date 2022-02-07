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

    // delete comment
    const commentsContainer = document.querySelector('.comments-container')
    deleteCommentBtns = document.querySelectorAll('.comment .fa-trash-alt')
    deleteCommentBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            commentId = parseInt(e.target.parentElement.dataset.id)
            
            fetch('/delete/comment/' + commentId)
                .then(res => res.json())
                .then(data => {
                    if (data.status_code === 200) {
                        // remove from DOM
                        console.log(data.msg)
                        commentsContainer.removeChild(e.target.parentElement) 
                    }
                })
        })
    })

    // search posts
    const searchInput = document.querySelector('#search-input')
    const searchBtn = document.querySelector('.fa-search')

    searchBtn.onclick = (e) => {
        const searchValue = searchInput.value
        console.log(window.location.href)
        window.location.href = window.location.origin + `/posts/filtered/${searchValue}/`
    }
    
    // toggle side bar functionality
    const toggleBtn = document.querySelector('.fa-bars')

    if (toggleBtn) {
        toggleBtn.onclick = () => {
            const sidebar = document.querySelector('#side-bar')
            if (sidebar.style.visibility == 'hidden') {
                sidebar.style.visibility = 'visible'
                sidebar.style.opacity = '1'
            }

            else {
                sidebar.style.visibility = 'hidden'
                sidebar.style.opacity = '0'
            }
        }
    }
}