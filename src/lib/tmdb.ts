const TMDB_API_KEY = process.env.NEXT_PUBLIC_TMDB_API_KEY
const BASE_URL = "https://api.themoviedb.org/3"

export async function fetchMovieDetails(movieId: number) {
  const res = await fetch(
    `${BASE_URL}/movie/${movieId}?api_key=${TMDB_API_KEY}`
  )

  if (!res.ok) {
    throw new Error("Failed to fetch movie")
  }

  return res.json()
}

export function getPosterUrl(path: string | null) {
  if (!path) return "/placeholder.png"
  return `https://image.tmdb.org/t/p/w500${path}`
}
