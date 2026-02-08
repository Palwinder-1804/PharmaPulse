import { useEffect, useState } from "react";
import { mockChartData, mockInfo, mockInsights, mockNews, mockSnippets } from "./utils/mock-data";
import Header from "./components/Header";
import NewsSection from "./components/NewSection";
import SearchBar from "./components/SearchBar";
import Sidebar from "./components/Sidebar";
import AnalyticsPage from "./components/AnalyticsPage";
import { setIntelligenceData, getIntelligenceData } from "./utils/mock-data";


export default function DashboardApp () {

  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [view, setView] = useState('dashboard');
  const [searchQuery, setSearchQuery] = useState('');
  

useEffect(() => {
  fetch("http://localhost:8000/api/intelligence")
    .then(res => res.json())
    .then(data => {
      setIntelligenceData(data);
      console.log("Fetched intelligence data from backend:", data);
      console.log("Stored in JS memory");
    });
}, []);

  const handleSearch = (query) => {
    setSearchQuery(query.toLowerCase().trim());
    setView('results');
  };

  const handleExpandNews = () => {
    setView('news');
  };

  const handleCollapseNews = () => {
    setView('dashboard');
  };

  return (
    <div className="min-h-screen bg-gray-50 flex">
      
      <Sidebar isOpen={sidebarOpen} onToggle={() => setSidebarOpen(!sidebarOpen)} setView={setView} />

      <div className="flex-1 flex flex-col min-w-0">
        <Header onMenuToggle={() => setSidebarOpen(true)} />

        <main className="flex-1 overflow-auto">
          <div className="h-full p-4 lg:p-8">
            
            {view === 'dashboard' && (
                <div className="grid grid-cols-1 lg:grid-cols-[1fr_320px] gap-6">

                  <div className="h-full flex flex-col gap-10">
                    <header className="w-full bg-background/80 backdrop-blur text-center">
                      <div className="max-w-7xl mx-auto px-6 py-4">
                        <h1 className="text-2xl font-black tracking-tight text-slate-800">
                          PharmaPulse
                        </h1>
                        <p className="text-sm text-slate-500">
                          Real-time pharma insights & updates
                        </p>
                      </div>
                    </header>
                    <div className="flex items-center justify-center">
                      <div className="w-full max-w-2xl px-4">
                        <SearchBar onSearch={handleSearch}  />
                      </div>
                    </div>
                  </div>

                  <div className="lg:block hidden">
                    <NewsSection 
                      isExpanded={false}
                      onExpand={handleExpandNews}
                    />
                  </div>
                </div>
            )}

            {view === 'results' && (
              <div className="h-full grid grid-cols-1 lg:grid-cols-3 gap-6">
                <AnalyticsPage searchQuery={searchQuery} />
                {!(view === 'results') && (
                  <div
                  className="col-span-1 lg:hidden"
                  >
                    <NewsSection 
                      isExpanded={false}
                      onExpand={handleExpandNews}
                    />
                  </div>
                )}
                
              </div>
            )}
            
            {view === 'news' && (
              <div className="w-full">
                <NewsSection 
                  isExpanded={true}
                  onCollapse={handleCollapseNews}
                />
              </div>
            )}
          </div>
        </main>
      </div>
    </div>
  );
};