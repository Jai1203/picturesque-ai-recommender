"use client"

import { useEffect, useState } from "react"
import { fetchMovieDetails, getPosterUrl } from "@/lib/tmdb"

type Props = {
  movieId: number
  selected: boolean
  onToggle: () => void
}

export default function MovieSelect({ movieId, selected, onToggle }: Props) {
  const [movie, setMovie] = useState<any>(null)

  useEffect(() => {
    fetchMovieDetails(movieId).then(setMovie)
  }, [movieId])

  if (!movie) return null

  return (
    <button
      onClick={onToggle}
      className={`w-40 rounded-lg overflow-hidden border transition ${
        selected ? "border-green-500" : "border-gray-700"
      }`}
    >
      <img
        src={getPosterUrl(movie.poster_path)}
        alt={movie.title}
        className="w-full h-60 object-cover"
      />
      <div className="p-2 text-sm text-center">
        {movie.title}
      </div>
    </button>
  )
}
