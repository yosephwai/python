import axios from "axios"

const listAnime = async () => {
    const anime = await axios.get('https://api.jikan.moe/v4/random/anime')
    return anime
}

listAnime().then(anime => console.log(anime.data.data.images.jpg))

