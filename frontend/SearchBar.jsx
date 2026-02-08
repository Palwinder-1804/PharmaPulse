import { Search } from "lucide-react";
import { useState } from "react";

export default function SearchBar ({ onSearch }) {
  const [query, setQuery] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (query.trim()) {
      onSearch(query);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="w-full max-w-2xl">
      <div className="relative">
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search for insights, reports, or analytics..."
          className="w-full px-6 py-4 pr-14 text-base border border-gray-300 rounded-xl
                   focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent
                   placeholder-gray-400 transition-shadow shadow-sm hover:shadow-md"
        />
        <button
          type="submit"
          className="absolute right-2 top-1/2 -translate-y-1/2 p-2.5 bg-blue-600 
                   text-white rounded-lg hover:bg-blue-700 transition-colors"
        >
          <Search size={20} />
        </button>
      </div>
    </form>
  );
};