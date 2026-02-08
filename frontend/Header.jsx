import { Menu } from "lucide-react";

export default function Header ({ onMenuToggle }) {
  return (
    <header className="h-16 bg-white border-b border-gray-200 flex items-center px-6 lg:px-8">
      <button 
        onClick={onMenuToggle}
        className="lg:hidden p-2 -ml-2 hover:bg-gray-100 rounded-lg transition-colors"
      >
        <Menu size={24} />
      </button>
      <h2 className="text-lg font-semibold text-gray-900 ml-2 lg:ml-0">Search & Insights</h2>
    </header>
  );
};